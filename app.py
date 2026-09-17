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
    .main-title {
        text-align: center;
        color: #1f4e79;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .matrix-title {
        text-align: center;
        color: #333;
        font-size: 24px;
        font-weight: bold;
    }

    .operator {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        padding-top: 120px;
    }

    .result-title {
        text-align: center;
        color: #1f4e79;
        font-size: 30px;
        font-weight: bold;
        margin-top: 30px;
    }

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
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">🔢 3 × 3 Matrix Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Perform matrix operations easily</div>',
    unsafe_allow_html=True
)


# =========================================================
# MATRIX INPUT FUNCTION
# =========================================================

def get_matrix(prefix):
    """
    Creates a 3 × 3 matrix of number input boxes.
    Returns the matrix as a list of lists.
    """

    matrix = []

    for i in range(3):

        cols = st.columns(3)

        row = []

        for j in range(3):

            with cols[j]:

                value = st.number_input(
                    f"Element {i + 1},{j + 1}",
                    value=0.0,
                    step=1.0,
                    key=f"{prefix}_{i}_{j}"
                )

                row.append(value)

        matrix.append(row)

    return matrix


# =========================================================
# MATRIX DISPLAY FUNCTION
# =========================================================

def display_matrix(matrix):
    """
    Displays a matrix using Streamlit's dataframe.
    """

    st.dataframe(
        matrix,
        hide_index=True,
        use_container_width=True
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

    # Matrix A
    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_add")

    # Operator
    with op:

        st.markdown(
            '<div class="operator">+</div>',
            unsafe_allow_html=True
        )

    # Matrix B
    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_add")

    st.markdown("")

    calculate = st.button(
        "➕ Calculate Addition",
        key="add_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(A[i][j] + B[i][j])

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

    # Matrix A
    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_sub")

    # Operator
    with op:

        st.markdown(
            '<div class="operator">−</div>',
            unsafe_allow_html=True
        )

    # Matrix B
    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_sub")

    st.markdown("")

    calculate = st.button(
        "➖ Calculate Subtraction",
        key="sub_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(A[i][j] - B[i][j])

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

    # Matrix A
    with col1:

        st.markdown(
            '<div class="matrix-title">Matrix A</div>',
            unsafe_allow_html=True
        )

        A = get_matrix("A_mul")

    # Operator
    with op:

        st.markdown(
            '<div class="operator">×</div>',
            unsafe_allow_html=True
        )

    # Matrix B
    with col2:

        st.markdown(
            '<div class="matrix-title">Matrix B</div>',
            unsafe_allow_html=True
        )

        B = get_matrix("B_mul")

    st.markdown("")

    calculate = st.button(
        "✖️ Calculate Multiplication",
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

                    value += A[i][k] * B[k][j]

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
        '<div class="matrix-title">Determinant of a 3 × 3 Matrix</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="matrix-title">Matrix A</div>',
        unsafe_allow_html=True
    )

    A = get_matrix("A_det")

    calculate = st.button(
        "📐 Calculate Determinant",
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

        st.markdown(
            f'<div class="det-result">{det_value:g}</div>',
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
        "🔄 Calculate Transpose",
        key="transpose_button",
        use_container_width=True
    )

    if calculate:

        result = []

        for i in range(3):

            row = []

            for j in range(3):

                row.append(A[j][i])

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
        '<div class="matrix-title">Inverse of a 3 × 3 Matrix</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="matrix-title">Matrix A</div>',
        unsafe_allow_html=True
    )

    A = get_matrix("A_inverse")

    calculate = st.button(
        "🔁 Calculate Inverse",
        key="inverse_button",
        use_container_width=True
    )

    if calculate:

        # Calculate determinant
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

        # Check whether inverse exists
        if abs(det_value) < 1e-10:

            st.error(
                "This matrix does not have an inverse because "
                "its determinant is 0."
            )

        else:

            # Cofactor matrix
            C = [
                [
                    A[1][1] * A[2][2] - A[1][2] * A[2][1],
                    -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
                    A[1][0] * A[2][1] - A[1][1] * A[2][0]
                ],
                [
                    -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
                    A[0][0] * A[2][2] - A[0][2] * A[2][0],
                    -(A[0][0] * A[2][1] - A[0][1] * A[2][0])
                ],
                [
                    A[0][1] * A[1][2] - A[0][2] * A[1][1],
                    -(A[0][0] * A[1][2] - A[0][2] * A[1][0]),
                    A[0][0] * A[1][1] - A[0][1] * A[1][0]
                ]
            ]

            # Adjugate = transpose of cofactor matrix
            adjugate = []

            for i in range(3):

                row = []

                for j in range(3):

                    row.append(C[j][i])

                adjugate.append(row)

            # Inverse = adjugate / determinant
            result = []

            for i in range(3):

                row = []

                for j in range(3):

                    row.append(adjugate[i][j] / det_value)

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
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    "<p style='text-align:center; color:gray;'>"
    "3 × 3 Matrix Calculator using Streamlit"
    "</p>",
    unsafe_allow_html=True
)
