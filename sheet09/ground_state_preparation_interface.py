import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli, Statevector

# This exercise has the goal the guide you through an implementation anyon creation
# Some interface is provided, fill out every TODO by replacing None, pass or []!
# Follow the protocol from exercise sheet 5, the name of the variables is this same.
# Do not rename the variables or change the data type of the output.
# No additional imports or packages are necessary.


L = 3  # the torus is L x L
n = 2 * L * L  # number of qubits = number of edges = n


def h(i, j) -> int:
    """
    Qubit on the horizontal edge from vertex (i, j) to (i+1, j).

    :param i: x-coordinate of the left end point of the edge; taken modulo L.
    :param j: y-coordinate (row) of the edge; taken modulo L.
    :return: index of the qubit on this edge, an even number in 0, ..., n-2.
    """
    #TODO
    return []


def v(i, j) -> int:
    """
    Qubit on the vertical edge from vertex (i, j) to (i, j+1).

    :param i: x-coordinate (column) of the edge; taken modulo L.
    :param j: y-coordinate of the lower end point of the edge; taken modulo L.
    :return: index of the qubit on this edge, an odd number in 1, ..., n-1.
    """
    #TODO
    return []


def star(i, j) -> list[int]:
    """
    The four edges that meet at vertex (i, j).

    :param i: x-coordinate of the vertex; taken modulo L.
    :param j: y-coordinate of the vertex; taken modulo L.
    :return: list of the four qubit indices [right, left, up, down].
    """
    #TODO
    return []


def plaquette(i, j) -> list[int]:
    """
    The four edges around the square with lower-left corner (i, j).

    :param i: x-coordinate of the lower-left corner of the square; taken modulo L.
    :param j: y-coordinate of the lower-left corner of the square; taken modulo L.
    :return: list of the four qubit indices [bottom, top, left, right].
    """
    #TODO
    return []


sites = [(i, j) for j in range(L) for i in range(L)]  # all vertices (and all squares), row by row

# Drawing helpers. You can use them without reading them.

ZC, XC = "#1F5BC6", "#8E44AD"
E_FILL, E_EDGE, M_FILL, M_EDGE = "#FFD23F", "#7A5A00", "#F28C28", "#8A4A0F"
GRID, VERTEX = "#C2C8D0", "#4B5563"


def edge_ends(q) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    The two end points of the edge that carries qubit q. This inverts h and v.

    :param q: qubit index in 0, ..., n-1 (even: horizontal edge, odd: vertical edge).
    :return: pair ((x0, y0), (x1, y1)) of the start and end vertex. The end point
        is not reduced modulo L, so it can lie on the right (x1 = L) or top
        (y1 = L) boundary of the picture.
    """
    k, vertical = divmod(q, 2)
    i, j = k % L, k // L
    #TODO
    return ((), ())


def edge_copies(q) -> list[tuple[tuple[int, int], tuple[int, int], float]]:
    """
    Where to draw edge q: the edge itself, plus a faded copy on the right
    (for a vertical edge in column 0) or at the top (for a horizontal edge in
    row 0), as a reminder of the periodic gluing.

    :param q: qubit index in 0, ..., n-1.
    :return: list of triples ((x0, x1), (y0, y1), alpha), one per copy. The first
        two entries are the x- and y-coordinates to pass to ax.plot, and alpha is
        the opacity: 1.0 for the edge itself, 0.45 for the faded copy.
    """
    (x0, y0), (x1, y1) = edge_ends(q)
    copies = [((x0, x1), (y0, y1), 1.0)]
    if x0 == x1 == 0:
        #TODO
        None
    if y0 == y1 == 0:
        #TODO
        None
    return copies


def draw_lattice(zs=(), xs=(), e=(), m=(), labels=False, title="", ax=None) -> None:
    """
    Draw the torus with strings and anyons. Z on an edge is drawn in blue, X as
    a wide purple band, an e as a yellow circle on a vertex and an m as an
    orange square in a plaquette. Faded copies on the right and at the top are
    reminders of the periodic gluing.

    :param zs: qubit indices carrying a Z, drawn as blue edges.
    :param xs: qubit indices carrying an X, drawn as purple bands.
    :param e: vertices (i, j) that hold an e anyon.
    :param m: plaquettes, given by their lower-left corner (i, j), that hold an m anyon.
    :param labels: if True, write the qubit index on every edge.
    :param title: title of the plot.
    :param ax: matplotlib Axes to draw into; defaults to the current axes.
    :return: None. The picture is drawn into ax.
    """
    ax = ax or plt.gca()
    for k in range(L):
        ax.plot([0, L], [k, k], color=GRID, lw=1, zorder=1)
        ax.plot([k, k], [0, L], color=GRID, lw=1, zorder=1)
    for q in xs:
        for xx, yy, a in edge_copies(q):
            ax.plot(xx, yy, color=XC, lw=8, alpha=0.4 * a, solid_capstyle="butt", zorder=2)
    for q in zs:
        for xx, yy, a in edge_copies(q):
            ax.plot(xx, yy, color=ZC, lw=3, alpha=a, solid_capstyle="round", zorder=3)
    if labels:
        for q in range(n):
            (x0, y0), (x1, y1) = edge_ends(q)
            ax.text((x0 + x1) / 2, (y0 + y1) / 2, str(q), ha="center", va="center", fontsize=8, zorder=5,
                    bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none"))
    ax.scatter(*zip(*sites), s=14, color=VERTEX, zorder=4)
    ghosts = [(L, k) for k in range(L + 1)] + [(k, L) for k in range(L)]  # copies of column 0 and row 0
    ax.scatter(*zip(*ghosts), s=14, facecolor="white", edgecolor=VERTEX, zorder=4)
    for (i, j) in e:
        for x, y, a in [(i, j, 1.0)] + ([(L, j, 0.45)] if i == 0 else []) + ([(i, L, 0.45)] if j == 0 else []):
            ax.scatter(x, y, s=260, color=E_FILL, edgecolor=E_EDGE, lw=1.5, alpha=a, zorder=6)
            ax.text(x, y, "e", ha="center", va="center", fontsize=10, alpha=a, zorder=7)
    for (i, j) in m:
        ax.scatter(i + 0.5, j + 0.5, s=240, marker="s", color=M_FILL, edgecolor=M_EDGE, lw=1.5, zorder=6)
        ax.text(i + 0.5, j + 0.5, "m", ha="center", va="center", fontsize=10, zorder=7)
    ax.set_xlim(-0.5, L + 0.5)
    ax.set_ylim(-0.5, L + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=10)


def part_2_the_lattice() -> None:
    """
    Part 2: The lattice.

    We take an L x L square lattice on a torus with L = 3: the right edge is
    glued to the left edge and the top to the bottom. There is one qubit on
    every edge, so 2 L^2 = 18 qubits in total.

    * Vertex (i, j): i counts to the right, j counts up, both modulo L.
    * h(i, j) is the horizontal edge from (i, j) to (i+1, j); v(i, j) is the
      vertical edge from (i, j) to (i, j+1).
    * The star A_v is the product of X on the four edges that meet at vertex v.
    * The plaquette B_p is the product of Z on the four edges around the square
      p; we label a square by its lower-left corner.

    The picture shows the qubit on every edge. The open circles on the right
    and at the top are the same vertices as those in column 0 and row 0. For
    example, the star at (0, 0) contains qubit 4, the edge from (2, 0) to
    (3, 0) = (0, 0).

    :return: None. Prints the qubits of the star and the plaquette at (0, 0)
        and shows the lattice with all qubit numbers.
    """
    print("number of qubits:", n)
    print("star at vertex (0,0) uses qubits   ", star(0, 0))
    print("plaquette at square (0,0) uses qubits", plaquette(0, 0))

    fig, ax = plt.subplots(figsize=(4.2, 4.2))
    draw_lattice(labels=True, title="the qubit on every edge", ax=ax)
    plt.show()


# ---------------------------------------------------------------------------
# Part 3: Stabilizers as Pauli operators
# ---------------------------------------------------------------------------

def pauli(kind, qubits) -> Pauli:
    """
    The Pauli operator kind on the listed qubits, identity on all others.
    Because Qiskit reads labels from the right, qubit q goes to position
    n - 1 - q of the label.

    :param kind: the letter 'X' or 'Z'.
    :param qubits: iterable of qubit indices in 0, ..., n-1 that carry kind.
    :return: the n-qubit Pauli operator, e.g. a star or a plaquette operator.
    """
    label = ["I"] * n
    for q in qubits:
        label[n - 1 - q] = kind
    return Pauli("".join(label))

A = {}  #TODO
B = {}  #TODO

def part_3_stabilizers() -> None:
    """
    Part 3: Stabilizers as Pauli operators.

    The helper pauli puts the letter X or Z on the listed qubits and I
    everywhere else. With it we build the 9 star operators A and the 9
    plaquette operators B, and check that every star commutes with every
    plaquette.

    Why do they commute? A star and a plaquette share either no edge or exactly
    two edges. On each shared edge X and Z anticommute, and two minus signs
    cancel.

    :return: None. Prints A and B at (0, 0) and whether all stars commute with
        all plaquettes.
    """
    print("A at (0,0):", A[(0, 0)])
    print("B at (0,0):", B[(0, 0)])
    print("every star commutes with every plaquette:",
          all(A[s].commutes(B[t]) for s in sites for t in sites))


# ---------------------------------------------------------------------------
# Part 4: The ground state
# ---------------------------------------------------------------------------

#TODO Zbar1 = pauli()  # a Z-loop around the torus, horizontally
#TODO Zbar2 = pauli()  # a Z-loop around the torus, vertically


def build_ground_circuit() -> QuantumCircuit:
    """
    Step 2 of part 4: fix the stars one at a time with a small circuit.

    Pick one edge of the star, the pivot, apply a Hadamard to it, and then
    CNOTs from the pivot to the other three edges. The Hadamard puts the pivot
    into a superposition of 0 and 1, and the CNOTs copy that bit to the other
    three edges. The result is a superposition of "nothing flipped" and "all
    four edges of the star flipped". Flipping all four edges is exactly what
    A_v does, so the state becomes

        |phi>  ->  (|phi> + A_v |phi>) / sqrt(2),   which has A_v = +1.

    This works as long as the pivot is still in |0> when we reach the star. We
    go through the vertices row by row and take as pivot the edge to the right,
    or the edge going up in the last column; with this order, no pivot has been
    touched before. The last star can be skipped: the product of all stars is
    the identity, so it comes out as +1 automatically.

    :return: circuit on n qubits that maps |0...0> to the ground state with
        Zbar_1 = Zbar_2 = +1.
    """
    ground_circuit = QuantumCircuit(n)
    for (i, j) in sites[:-1]:  # every star except the last one
        None
        #Todo

    return ground_circuit


def part_4_ground_state() -> tuple[QuantumCircuit, Statevector]:
    """
    Part 4: The ground state.

    The Hamiltonian is H = -(sum over v of A_v) - (sum over p of B_p), so a
    ground state has A_v = +1 for every star and B_p = +1 for every plaquette.

    Step 1. Start with all qubits in |0>. Since Z|0> = |0>, every plaquette is
    already +1. The stars are not: their expectation values are 0.

    Step 2. Fix the stars with the circuit from build_ground_circuit. Afterwards
    every star and every plaquette is +1: we are in the ground space.

    Which ground state? On the torus the ground space is 4-dimensional: it
    holds two logical qubits. They are read by loops of Z around the torus,
    Zbar_1 along the bottom row of horizontal edges and Zbar_2 along the left
    column of vertical edges. Our circuit prepares the ground state with
    Zbar_1 = Zbar_2 = +1.

    :return: pair (ground_circuit, ground): the preparation circuit from
        build_ground_circuit and the ground state it produces.
    """
    zero = Statevector.from_label("0" * n)
    print("<B_p> in |0...0>:", [round(zero.expectation_value(B[s]).real) for s in sites])
    print("<A_v> in |0...0>:", [round(zero.expectation_value(A[s]).real) for s in sites])

    ground_circuit = build_ground_circuit()
    ground_circuit.draw("mpl", fold=-1, scale=0.55)
    plt.show()

    ground = Statevector(ground_circuit)
    print("<A_v>:", [round(ground.expectation_value(A[s]).real) for s in sites])
    print("<B_p>:", [round(ground.expectation_value(B[s]).real) for s in sites])
    print("<Zbar_1> =", round(ground.expectation_value(Zbar1).real),
          "   <Zbar_2> =", round(ground.expectation_value(Zbar2).real))
    return ground_circuit, ground


def test_torus_3x3() -> None:
    """
    Test the 3 x 3 torus: the periodic gluing at the corners (0, 0) and (2, 2),
    every edge on exactly two stars and two plaquettes, all stars commuting with
    all plaquettes, and A_v = B_p = Zbar_1 = Zbar_2 = +1 in the prepared state.

    :return: None. Raises an AssertionError if a check fails.
    """
    assert (L, n) == (3, 18)
    assert star(0, 0) == [0, 4, 1, 13] and plaquette(2, 2) == [16, 4, 17, 13]
    for edges_of in (star, plaquette):
        incidences = [q for s in sites for q in edges_of(*s)]
        assert all(incidences.count(q) == 2 for q in range(n))
    assert all(A[s].commutes(B[t]) for s in sites for t in sites)
    ground = Statevector(build_ground_circuit())
    assert all(abs(ground.expectation_value(P) - 1) < 1e-9 for P in [*A.values(), *B.values(), Zbar1, Zbar2])


if __name__ == "__main__":
    test_torus_3x3()
    print("3 x 3 torus test passed")