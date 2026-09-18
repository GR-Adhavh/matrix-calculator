import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="3 × 3 Matrix Calculator",
    page_icon="🔢",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Main title */
    .main-title {
        text-align: center;
        color: #1f4e79;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Matrix heading */
    .matrix-title {
        text-align: center;
        color: #333;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Matrix input boxes */
    div[data-testid="stNumberInput"] {
        margin-bottom: 0px;
    }

    div[data-testid="stNumberInput"] input {
        text-align: center;
        font-size: 20px;
        font-weight: 500;
        height: 48px;
    }

    /* Hide number input labels */
    div[data-testid="stNumberInput"] label {
        display: none;
    }

    /* Matrix brackets */
    .bracket {
        font-size: 90px;
        line-height: 1;
        color: #333;
        font-weight: 200;
    }

    .bracket-left {
        margin-right: -10px;
    }

    .bracket-right {
        margin-left: -10px;
    }

    /* Operator */
    .operator {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        padding-top: 120px;
    }

    /* Result heading */
    .result-title {
        text-align: center;
        color: #1f4e79;
        font-size: 30px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    /* Determinant result */
    .det-result {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #008000;
        padding: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MATRIX INPUT FUNCTION
# =========================================================

def get_matrix(prefix):
    """
    Creates a 3 × 3 matrix of number input boxes.
    The inputs are visually arranged like a matrix.
    """

    matrix = []

    # Matrix input area without brackets
    matrix_area = st.container()

    with matrix_area:

        for i in range(3):

            cols = st.columns(3)

            row = []

            for j in range(3):

                with cols[j]:

                    value = st.number_input(
                        "",
                        value=0.0,
                        step=1.0,
                        key=f"{prefix}_{i}_{j}",
                        label_visibility="collapsed"
                    )

                    row.append(value)

            matrix.append(row)

    return matrix


# =========================================================
# MATRIX DISPLAY FUNCTION
# =========================================================

def display_matrix(matrix):

    st.markdown(
        """
        <style>
        .result-matrix {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 15px auto 30px auto;
        }

        .result-bracket {
            font-size: 100px;
            font-weight: 200;
            line-height: 0.8;
            color: #333;
        }

        .result-table {
            border-collapse: collapse;
            margin: 0 8px;
        }

        .result-table td {
            padding: 10px 25px;
            text-align: center;
            font-size: 22px;
            min-width: 70px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Format values properly
    formatted_matrix = []

    for row in matrix:

        formatted_row = []

        for value in row:

            value = float(value)

            if value.is_integer():
                formatted_row.append(str(int(value)))
            else:
                formatted_row.append(f"{value:.6f}".rstrip("0").rstrip("."))

        formatted_matrix.append(formatted_row)

    # Use Streamlit columns instead of raw HTML table
    col_left, col_matrix, col_right = st.columns([1, 6, 1])

    with col_left:
        st.markdown(
            '<div class="result-bracket">[</div>',
            unsafe_allow_html=True
        )

    with col_matrix:

        for row in formatted_matrix:

            cols = st.columns(3)

            for j in range(3):

                with cols[j]:
                    st.markdown(
                        f"<div style='text-align:center; "
                        f"font-size:22px; padding:10px;'>"
                        f"{row[j]}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

    with col_right:
        st.markdown(
            '<div class="result-bracket">]</div>',
            unsafe_allow_html=True
        )


# =========================================================
# MATRIX ADDITION
# =========================================================

def add():

    st.markdown(
        '<div class="matrix-title">Matrix Addition</div>',
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    # -----------------------------------------------------
    # Matrix A
    # -----------------------------------------------------

    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_add")

    # -----------------------------------------------------
    # Operator
    # -----------------------------------------------------

    with op:

        st.markdown(
            '<div class="operator">+</div>',
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # Matrix B
    # -----------------------------------------------------

    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_add")

    st.markdown("")

    calculate = st.button(
        "Calculate",
        key="add_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(
                    A[i][j] + B[i][j]
                )

            result.append(row)

        st.markdown(
            '<div class="result-title">Result</div>',
            unsafe_allow_html=True
        )

        display_matrix(result)


# =========================================================
# MATRIX SUBTRACTION
# =========================================================

def sub():

    st.markdown(
        '<div class="matrix-title">Matrix Subtraction</div>',
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    # -----------------------------------------------------
    # Matrix A
    # -----------------------------------------------------

    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_sub")

    # -----------------------------------------------------
    # Operator
    # -----------------------------------------------------

    with op:

        st.markdown(
            '<div class="operator">−</div>',
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # Matrix B
    # -----------------------------------------------------

    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_sub")

    st.markdown("")

    calculate = st.button(
        "Calculate",
        key="sub_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(
                    A[i][j] - B[i][j]
                )

            result.append(row)

        st.markdown(
            '<div class="result-title">Result</div>',
            unsafe_allow_html=True
        )

        display_matrix(result)


# =========================================================
# MATRIX MULTIPLICATION
# =========================================================

def mul():

    st.markdown(
        '<div class="matrix-title">Matrix Multiplication</div>',
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    # -----------------------------------------------------
    # Matrix A
    # -----------------------------------------------------

    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_mul")

    # -----------------------------------------------------
    # Operator
    # -----------------------------------------------------

    with op:

        st.markdown(
            '<div class="operator">×</div>',
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # Matrix B
    # -----------------------------------------------------

    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_mul")

    st.markdown("")

    calculate = st.button(
        "Calculate",
        key="mul_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                value = 0

                for k in range(3):

                    value += (
                        A[i][k] * B[k][j]
                    )

                row.append(value)

            result.append(row)

        st.markdown(
            '<div class="result-title">Result</div>',
            unsafe_allow_html=True
        )

        display_matrix(result)


# =========================================================
# DETERMINANT
# =========================================================

def determinant():

    st.markdown(
        '<div class="matrix-title">Determinant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="matrix-title">Matrix A</div>',
        unsafe_allow_html=True
    )

    A = get_matrix("A_det")

    calculate = st.button(
        "Calculate",
        key="det_button",
        use_container_width=True
    )

    if calculate:

        det_value = (
            A[0][0] * (
                A[1][1] * A[2][2]
                - A[1][2] * A[2][1]
            )
            - A[0][1] * (
                A[1][0] * A[2][2]
                - A[1][2] * A[2][0]
            )
            + A[0][2] * (
                A[1][0] * A[2][1]
                - A[1][1] * A[2][0]
            )
        )

        st.markdown(
            '<div class="result-title">Determinant</div>',
            unsafe_allow_html=True
        )

        if float(det_value).is_integer():

            det_display = int(det_value)

        else:

            det_display = round(det_value, 6)

        st.markdown(
            f'<div class="det-result">{det_display}</div>',
            unsafe_allow_html=True
        )


# =========================================================
# TRANSPOSE
# =========================================================

def transpose():

    st.markdown(
        '<div class="matrix-title">Matrix Transpose</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="matrix-title">Matrix A</div>',
        unsafe_allow_html=True
    )

    A = get_matrix("A_transpose")

    calculate = st.button(
        "Calculate",
        key="transpose_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(
                    A[j][i]
                )

            result.append(row)

        st.markdown(
            '<div class="result-title">Transpose</div>',
            unsafe_allow_html=True
        )

        display_matrix(result)


# =========================================================
# INVERSE
# =========================================================

def inverse():

    st.markdown(
        '<div class="matrix-title">Matrix Inverse</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="matrix-title">Matrix A</div>',
        unsafe_allow_html=True
    )

    A = get_matrix("A_inverse")

    calculate = st.button(
        "Calculate",
        key="inverse_button",
        use_container_width=True
    )

    if calculate:

        # -------------------------------------------------
        # Determinant
        # -------------------------------------------------

        det_value = (
            A[0][0] * (
                A[1][1] * A[2][2]
                - A[1][2] * A[2][1]
            )
            - A[0][1] * (
                A[1][0] * A[2][2]
                - A[1][2] * A[2][0]
            )
            + A[0][2] * (
                A[1][0] * A[2][1]
                - A[1][1] * A[2][0]
            )
        )

        # -------------------------------------------------
        # Check determinant
        # -------------------------------------------------

        if abs(det_value) < 1e-10:

            st.error(
                "The inverse does not exist because "
                "the determinant of the matrix is 0."
            )

            return

        # -------------------------------------------------
        # Cofactor Matrix
        # -------------------------------------------------

        C = [

            [
                A[1][1] * A[2][2]
                - A[1][2] * A[2][1],

                -(A[1][0] * A[2][2]
                  - A[1][2] * A[2][0]),

                A[1][0] * A[2][1]
                - A[1][1] * A[2][0]
            ],

            [
                -(A[0][1] * A[2][2]
                  - A[0][2] * A[2][1]),

                A[0][0] * A[2][2]
                - A[0][2] * A[2][0],

                -(A[0][0] * A[2][1]
                  - A[0][1] * A[2][0])
            ],

            [
                A[0][1] * A[1][2]
                - A[0][2] * A[1][1],

                -(A[0][0] * A[1][2]
                  - A[0][2] * A[1][0]),

                A[0][0] * A[1][1]
                - A[0][1] * A[1][0]
            ]
        ]

        # -------------------------------------------------
        # Adjugate Matrix
        # -------------------------------------------------

        adjugate = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(
                    C[j][i]
                )

            adjugate.append(row)

        # -------------------------------------------------
        # Inverse Matrix
        # -------------------------------------------------

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(
                    adjugate[i][j] / det_value
                )

            result.append(row)

        st.markdown(
            '<div class="result-title">Inverse</div>',
            unsafe_allow_html=True
        )

        display_matrix(result)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🔢 Matrix Calculator")

operation = st.sidebar.radio(
    "Select Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Determinant",
        "Transpose",
        "Inverse"
    ]
)


# =========================================================
# RUN SELECTED OPERATION
# =========================================================

if operation == "Addition":

    add()

elif operation == "Subtraction":

    sub()

elif operation == "Multiplication":

    mul()

elif operation == "Determinant":

    determinant()

elif operation == "Transpose":

    transpose()

elif operation == "Inverse":

    inverse()


# =========================================================
# ARROW KEY NAVIGATION
# =========================================================

st.markdown(
    """
    <script>
    (function() {

        function setupMatrixNavigation() {

            const inputs = Array.from(
                window.parent.document.querySelectorAll(
                    'input[type="number"]'
                )
            );

            if (inputs.length === 0) {
                return;
            }

            inputs.forEach(function(input) {

                if (input.dataset.arrowNavigation === "true") {
                    return;
                }

                input.dataset.arrowNavigation = "true";

                input.addEventListener("keydown", function(event) {

                    const currentIndex = inputs.indexOf(input);

                    if (currentIndex === -1) {
                        return;
                    }

                    let targetIndex = -1;

                    /*
                     * Matrix has 3 columns.
                     *
                     * Right  -> next element
                     * Left   -> previous element
                     * Down   -> same column, next row
                     * Up     -> same column, previous row
                     */

                    if (event.key === "ArrowRight") {

                        targetIndex = currentIndex + 1;

                    } else if (event.key === "ArrowLeft") {

                        targetIndex = currentIndex - 1;

                    } else if (event.key === "ArrowDown") {

                        targetIndex = currentIndex + 3;

                    } else if (event.key === "ArrowUp") {

                        targetIndex = currentIndex - 3;

                    } else {

                        return;
                    }

                    /*
                     * Don't move outside the current matrix.
                     */

                    if (
                        targetIndex >= 0 &&
                        targetIndex < inputs.length
                    ) {

                        event.preventDefault();

                        inputs[targetIndex].focus();

                        inputs[targetIndex].select();
                    }

                });

            }

        }

        setupMatrixNavigation();

        /*
         * Streamlit reruns the page when values change,
         * so check again periodically for newly-created inputs.
         */

        setInterval(
            setupMatrixNavigation,
            500
        );

    })();
    </script>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <p style="text-align:center; color:gray;">
        3 × 3 Matrix Calculator using Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
