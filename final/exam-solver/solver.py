"""QIT Final Exam Part II — solver (validation script).

Implements the 10 questions + bonus, parameterized by the exam inputs.
Theory references: course lectures C4-C7 (see final/proofs/).
"""
import numpy as np
from scipy.linalg import sqrtm, eigh

TOL = 1e-9
GROUP_TOL = 1e-6


# ----------------------------- helpers -----------------------------
def xlog2x(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    m = x > TOL
    out[m] = x[m] * np.log2(x[m])
    return out


def vn_entropy(rho):
    """von Neumann entropy in bits."""
    w = eigh(rho, eigvals_only=True)
    w = np.clip(w.real, 0, None)
    w = w / w.sum()  # guard normalization
    return float(-xlog2x(w).sum())


def shannon(probs):
    p = np.clip(np.asarray(probs, float), 0, None)
    p = p / p.sum()
    return float(-xlog2x(p).sum())


def normalize(vec, norm):
    v = np.asarray(vec, dtype=complex)
    return v / np.sqrt(norm)


def proj(v):
    v = v.reshape(-1, 1)
    return v @ v.conj().T


def spectral_projectors(O):
    """Return list of (eigenvalue, projector) grouped by distinct eigenvalue."""
    w, V = eigh(O)
    groups = []
    for i, lam in enumerate(w):
        placed = False
        for g in groups:
            if abs(g["lam"] - lam) < GROUP_TOL:
                g["vecs"].append(V[:, i]); placed = True; break
        if not placed:
            groups.append({"lam": float(lam), "vecs": [V[:, i]]})
    res = []
    for g in groups:
        P = np.zeros_like(O, dtype=complex)
        for u in g["vecs"]:
            P += proj(u)
        res.append((g["lam"], P))
    return res


def fidelity(rho, sigma):
    """Uhlmann fidelity, SQUARED convention: (Tr sqrt(sqrt(rho) sigma sqrt(rho)))^2."""
    sr = sqrtm(rho)
    inner = sr @ sigma @ sr
    s = sqrtm(inner)
    val = np.real(np.trace(s))
    return float(np.clip(val, 0, 1) ** 2)


def partial_transpose_B(rho, dA=2, dB=2):
    R = rho.reshape(dA, dB, dA, dB)
    RT = R.transpose(0, 3, 2, 1)  # transpose B indices
    return RT.reshape(dA * dB, dA * dB)


# ----------------------------- channel -----------------------------
def build_channel(O):
    projs = spectral_projectors(O)
    I = np.eye(O.shape[0], dtype=complex)

    def Delta(rho):
        return sum(P @ rho @ P for _, P in projs)

    def E(rho):
        return 0.5 * rho + 0.5 * Delta(rho)

    # Kraus operators of E
    kraus = [np.sqrt(0.5) * I] + [np.sqrt(0.5) * P for _, P in projs]
    return E, kraus, projs


def choi(E, d=4):
    """Choi matrix J = (I ⊗ E)(|Omega><Omega|), |Omega> = sum_i |i>|i> (unnormalized)."""
    J = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            Eij = E(basis_ket(i, d) @ basis_ket(j, d).conj().T)
            # place E(|i><j|) into block (i,j)
            J[i * d:(i + 1) * d, j * d:(j + 1) * d] = Eij
    return J


def basis_ket(i, d):
    e = np.zeros((d, 1), dtype=complex); e[i, 0] = 1.0
    return e


def purify(rho):
    """Return |Omega> in C^d ⊗ C^d purifying rho."""
    w, V = eigh(rho)
    w = np.clip(w.real, 0, None)
    d = rho.shape[0]
    ket = np.zeros((d * d, 1), dtype=complex)
    for i in range(d):
        if w[i] > TOL:
            ket += np.sqrt(w[i]) * np.kron(V[:, i].reshape(-1, 1), basis_ket(i, d))
    return ket


# ----------------------------- witness (Q2) -----------------------------
def is_psd(M):
    return np.min(eigh(M, eigvals_only=True).real) > -1e-9


def min_product_expectation(O, restarts=400, seed=0):
    """min over product states |a>⊗|b> of <ab|O|ab>, via random restarts + local refine."""
    rng = np.random.default_rng(seed)
    best = np.inf

    def rand_qubit():
        v = rng.standard_normal(2) + 1j * rng.standard_normal(2)
        return v / np.linalg.norm(v)

    def expect(a, b):
        psi = np.kron(a, b).reshape(-1, 1)
        return float(np.real((psi.conj().T @ O @ psi)[0, 0]))

    for _ in range(restarts):
        a, b = rand_qubit(), rand_qubit()
        val = expect(a, b)
        # a few rounds of coordinate descent: optimal a is min-eigvec of reduced operator
        for _ in range(50):
            # fix b -> operator on a: O_a[i,i'] = sum_{j,j'} b*_j O_{ij,i'j'} b_{j'}
            Ob = np.einsum('j, k,ijkl->il', b.conj(), b,
                           O.reshape(2, 2, 2, 2)).reshape(2, 2)
            wa, Va = eigh(Ob); a = Va[:, 0]
            Oa = np.einsum('i,k,ijkl->jl', a.conj(), a,
                           O.reshape(2, 2, 2, 2)).reshape(2, 2)
            wb, Vb = eigh(Oa); b = Vb[:, 0]
            nv = expect(a, b)
            if abs(nv - val) < 1e-12:
                val = nv; break
            val = nv
        best = min(best, val)
    return best


def q2_witness(rho_v, O):
    pt = partial_transpose_B(rho_v)
    min_pt = float(np.min(eigh(pt, eigvals_only=True).real))
    entangled = min_pt < -1e-9

    herm = np.allclose(O, O.conj().T)
    O_has_neg = np.min(eigh(O, eigvals_only=True).real) < -1e-9
    block_pos = min_product_expectation(O) > -1e-6
    valid_witness = herm and O_has_neg and block_pos

    trace_Orho = float(np.real(np.trace(O @ rho_v)))
    detects = trace_Orho < -1e-9

    if not entangled:
        letter = "D (separable)"
    elif valid_witness and detects:
        letter = "A (witnessed by O)"
    elif valid_witness and not detects:
        letter = "B (not witnessed by O)"
    else:
        letter = "C (entangled but O not a witness)"
    return dict(entangled=entangled, min_pt=min_pt, valid_witness=valid_witness,
                block_pos=block_pos, O_has_neg=O_has_neg,
                trace_Orho=trace_Orho, detects=detects, letter=letter)


# ----------------------------- bonus -----------------------------
def h2(x):
    if x <= 0 or x >= 1:
        return 0.0
    return float(-x * np.log2(x) - (1 - x) * np.log2(1 - x))


def bonus(delta_bit, delta_phase, eps_target, key_length=256):
    rhs = 1 - 0.5 * h2(delta_bit) - 0.5 * h2(delta_phase)  # lower bound on h(p)
    rhs = max(rhs, 0.0)
    # p <= 1/2 (1 + sqrt(ln2 (h(dbit)+h(dphase))))
    p = 0.5 * (1 + np.sqrt(np.log(2) * (h2(delta_bit) + h2(delta_phase))))
    p = min(p, 1.0)
    return dict(h_p_lower=rhs, p_per_bit=p, p_key=p ** key_length)


# ----------------------------- main solve -----------------------------
def solve(inp):
    phi = normalize(inp["phi_raw"], inp["phi_norm"])
    psi = normalize(inp["psi_raw"], inp["psi_norm"])
    w0, w1 = inp["v_weights"]
    O = inp["O_prefactor"] * np.array(inp["O_matrix"], dtype=complex)

    rho_v = w0 * proj(phi) + w1 * proj(psi)
    E, kraus, projs = build_channel(O)
    rho_w = E(rho_v)

    ans = {}

    # Q1 entanglement entropy of |psi>
    M = psi.reshape(2, 2)
    rho_A = M @ M.conj().T
    ans["Q1"] = vn_entropy(rho_A)

    # Q2 witness
    q2 = q2_witness(rho_v, O)
    ans["Q2"] = q2["letter"]; ans["_Q2"] = q2

    # Q3 Schumacher H(rho_v)
    ans["Q3"] = vn_entropy(rho_v)

    # Q4/Q5 measure O distribution
    p_lambda = np.array([np.real(np.trace(P @ rho_v)) for _, P in projs])
    p_lambda = np.clip(p_lambda, 0, None); p_lambda /= p_lambda.sum()
    ans["Q4"] = shannon(p_lambda)
    ans["Q5"] = float(np.sum(p_lambda ** 2))

    # Q6 max-basis collision = Tr(rho^2)
    ans["Q6"] = float(np.real(np.trace(rho_v @ rho_v)))

    # Q7 minimal Kraus = Choi rank
    J = choi(E, 4)
    evJ = eigh(J, eigvals_only=True).real
    ans["Q7"] = int(np.sum(evJ > 1e-7))

    # Q8 fidelity F(rho_v, rho_w)  [squared, course/Uhlmann convention]
    ans["Q8"] = fidelity(rho_v, rho_w)
    # also expose the UNSQUARED fidelity Tr|sqrt(rho_v) sqrt(rho_w)| (Nielsen-Chuang /
    # generalized-fidelity convention) = sqrt of the squared one
    ans["Q8_unsquared"] = float(np.sqrt(ans["Q8"]))

    # Q9 entanglement fidelity
    Fe = sum(abs(np.trace(K @ rho_v)) ** 2 for K in kraus)
    ans["Q9"] = float(np.real(Fe))

    # Q10 entropy exchange = H(W), W[k,l]=Tr(K_k rho K_l^dag)
    m = len(kraus)
    W = np.zeros((m, m), dtype=complex)
    for k in range(m):
        for l in range(m):
            W[k, l] = np.trace(kraus[k] @ rho_v @ kraus[l].conj().T)
    ans["Q10"] = vn_entropy(W)

    # cross-checks for Q9/Q10 via purification.
    # purify() builds |Omega> = sum sqrt(w_i) |V_i>_sys ⊗ |i>_ref, so the SYSTEM
    # is the FIRST tensor factor. The channel acts on the system => apply E across
    # the first-factor indices for each fixed reference index.
    Omega = purify(rho_v)
    d = 4
    Om = (Omega @ Omega.conj().T).reshape(d, d, d, d)  # [sys, ref, sys', ref']
    out = np.zeros((d, d, d, d), dtype=complex)
    for r in range(d):
        for rp in range(d):
            block = Om[:, r, :, rp]          # d x d matrix in system indices
            out[:, r, :, rp] = E(block)
    rho_RB = out.reshape(d * d, d * d)
    ans["_Q9_check"] = float(np.real((Omega.conj().T @ rho_RB @ Omega)[0, 0]))
    ans["_Q10_check"] = vn_entropy(rho_RB)

    ans["_bonus"] = bonus(inp["delta_bit"], inp["delta_phase"],
                          inp["eps_target"], inp.get("key_length", 256))
    return ans


def closest(val, options):
    if not isinstance(val, (int, float)):
        return val, None
    best = min(options.items(), key=lambda kv: abs(kv[1] - val))
    return best[0], abs(best[1] - val)


# ----------------------------- variants -----------------------------
VARIANTS = {
    "3109": dict(
        phi_raw=[13, 6, 6, 22], phi_norm=725, psi_raw=[-27, 16, 16, -3], psi_norm=1250,
        v_weights=(203/703, 500/703), O_prefactor=1,
        O_matrix=[[7, 0, 0, 6], [0, 25, 0, 0], [0, 0, 25, 0], [6, 0, 0, 23]],
        delta_bit=0.08, delta_phase=0.02, eps_target=1e-6,
        options={
            "Q1": dict(A=0.867117, B=0.141441, C=1.742312, D=1.441988),
            "Q3": dict(A=0.831474, B=1.878090, C=0.576334, D=0.867117),
            "Q4": dict(A=0.622528, B=0.540508, C=0.780658, D=0.940744),
            "Q5": dict(A=0.540508, B=0.940744, C=0.780658, D=0.622528),
            "Q6": dict(A=0.589243, B=0.612188, C=0.285043, D=0.500000),
            "Q8": dict(A=0.770254, B=0.901849, C=0.877641, D=0.813331),
            "Q9": dict(A=0.813331, B=0.901849, C=0.770254, D=0.877641),
            "Q10": dict(A=0.762480, B=0.970372, C=1.427005, D=0.595530),
        }),
    "3992": dict(
        phi_raw=[7, 4, 4, 13], phi_norm=250, psi_raw=[-14, 22, 22, 19], psi_norm=1525,
        v_weights=(100/161, 61/161), O_prefactor=1,
        O_matrix=[[125, -48, 14, -20], [-48, 51, -48, -96], [14, -48, 29, 28], [-20, -96, 28, 95]],
        delta_bit=0.03, delta_phase=0.10, eps_target=1e-3,
        options={
            "Q1": dict(A=1.923481, B=1.978104, C=0.957249, D=0.976414),
            "Q3": dict(A=0.523586, B=0.957249, C=1.695174, D=0.755375),
            "Q4": dict(A=1.204394, B=1.541922, C=0.428087, D=0.480862),
            "Q5": dict(A=0.480862, B=0.428087, C=1.204394, D=1.541922),
            "Q6": dict(A=0.326565, B=0.500000, C=0.529339, D=0.659735),
            "Q8": dict(A=0.714044, B=0.819843, C=0.845011, D=0.905452),
            "Q9": dict(A=0.819843, B=0.905452, C=0.845011, D=0.714044),
            "Q10": dict(A=1.199432, B=0.636067, C=1.391442, D=1.270961),
        }),
    "6572": dict(
        phi_raw=[21, -8, -8, 9], phi_norm=650, psi_raw=[-1, 2, 2, 2], psi_norm=13,
        v_weights=(5/17, 12/17), O_prefactor=1,
        O_matrix=[[77, 0, -20, 32], [0, 9, 0, 0], [-20, 0, 17, -20], [32, 0, -20, 77]],
        delta_bit=0.02, delta_phase=0.05, eps_target=1e-6,
        options={
            "Q1": dict(A=1.854286, B=1.950212, C=0.873981, D=0.890492),
            "Q3": dict(A=0.540204, B=0.873981, C=1.844665, D=0.779350),
            "Q4": dict(A=1.505731, B=0.573119, C=0.951219, D=0.371714),
            "Q5": dict(A=0.371714, B=0.573119, C=0.951219, D=1.505731),
            "Q6": dict(A=0.644970, B=0.584775, C=0.500000, D=0.307159),
            "Q8": dict(A=0.902357, B=0.814248, C=0.828165, D=0.685857),
            "Q9": dict(A=0.902357, B=0.828165, C=0.814248, D=0.685857),
            "Q10": dict(A=1.252865, B=1.416094, C=1.189328, D=0.636744),
        }),
    "6223": dict(
        phi_raw=[9, 8, 8, 21], phi_norm=650, psi_raw=[-21, 28, 28, 21], psi_norm=2450,
        v_weights=(13/18, 5/18), O_prefactor=1,
        O_matrix=[[191, -12, -80, 2], [-12, 93, -24, -12], [-80, -24, 113, -80], [2, -12, -80, 191]],
        delta_bit=0.09, delta_phase=0.07, eps_target=1e-5,
        options={
            "Q1": dict(A=0.852405, B=1.000000, C=1.985228, D=1.942683),
            "Q3": dict(A=0.650022, B=1.634857, C=0.852405, D=0.450561),
            "Q4": dict(A=1.540656, B=0.440299, C=0.410282, D=1.405083),
            "Q5": dict(A=1.540656, B=1.405083, C=0.440299, D=0.410282),
            "Q6": dict(A=0.722222, B=0.500000, C=0.339999, D=0.598765),
            "Q8": dict(A=0.814600, B=0.902552, C=0.705141, D=0.839727),
            "Q9": dict(A=0.814600, B=0.902552, C=0.839727, D=0.705141),
            "Q10": dict(A=1.360507, B=0.710485, C=1.202687, D=1.270328),
        }),
}


if __name__ == "__main__":
    for vid, inp in VARIANTS.items():
        ans = solve(inp)
        print(f"\n================ Variant {vid} ================")
        opts = inp["options"]
        for q in ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]:
            val = ans[q]
            if q in opts:
                letter, gap = closest(val, opts[q])
                flag = "" if (gap is not None and gap < 1e-3) else "  <-- CHECK"
                print(f"  {q}: {val!s:<24} -> {letter}  (gap {gap:.2e}){flag}")
            else:
                print(f"  {q}: {val}")
        print(f"  Q2 detail: {ans['_Q2']}")
        print(f"  Q9 check (purif): {ans['_Q9_check']:.6f} ; Q10 check: {ans['_Q10_check']:.6f}")
        b = ans["_bonus"]
        print(f"  Bonus: p_per_bit={b['p_per_bit']:.6f}  p_key={b['p_key']:.3e}")
