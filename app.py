import streamlit as st


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="3 × 3 Matrix Calculator",
    page_icon="🔢",
    layout="wide"
)


# ---------------------------------------------------------
# MATRIX INPUT FUNCTION
# ---------------------------------------------------------

def get_matrix(prefix):
    """
    Creates a 3x3 matrix of input boxes.
    The inputs are visually aligned like a matrix.
    """

    matrix = []

    for i in range(3):
        cols = st.columns([1, 1, 1])

        row = []

        for j in range(3):
            with cols[j]:
                value = st.number_input(
                    "",
                    value=0,
                    step=1,
                    key=f"{prefix}_{i}_{j}",
                    label_visibility="collapsed"
                )

                row.append(value)

        matrix.append(row)

    return matrix


# ---------------------------------------------------------
# DISPLAY MATRIX
# ---------------------------------------------------------

def display_matrix(matrix, title=""):
    """
    Displays a matrix with brackets around it.
    """

    if title:
        st.markdown(
            f"<h3 style='text-align:center;'>{title}</h3>",
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <style>
        .matrix-bracket {
            font-size: 70px;
            line-height: 1;
            color: #444;
        }

        .matrix-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: -20px;
            margin-bottom: 20px;
        }

        .matrix-result {
            font-size: 22px;
            text-align: center;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# ADDITION
# ---------------------------------------------------------

def add():

    st.markdown(
        "<h2 style='text-align:center;'>Matrix Addition</h2>",
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    with col1:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix A</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px; line-height:0.5;'>[</div>",
            unsafe_allow_html=True
        )

        A = get_matrix("A_add")

        st.markdown(
            "<div style='text-align:center; font-size:70px; line-height:0.5;'>]</div>",
            unsafe_allow_html=True
        )

    with op:

        st.markdown(
            "<div style='font-size:45px; text-align:center; padding-top:100px;'>+</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix B</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px; line-height:0.5;'>[</div>",
            unsafe_allow_html=True
        )

        B = get_matrix("B_add")

        st.markdown(
            "<div style='text-align:center; font-size:70px; line-height:0.5;'>]</div>",
            unsafe_allow_html=True
        )

    st.markdown("")

    calculate = st.button(
        "Calculate",
        key="add_button",
        use_container_width=True
    )

    if calculate:

        A11 = A[0][0] + B[0][0]
        A12 = A[0][1] + B[0][1]
        A13 = A[0][2] + B[0][2]

        A21 = A[1][0] + B[1][0]
        A22 = A[1][1] + B[1][1]
        A23 = A[1][2] + B[1][2]

        A31 = A[2][0] + B[2][0]
        A32 = A[2][1] + B[2][1]
        A33 = A[2][2] + B[2][2]

        result = [
            [A11, A12, A13],
            [A21, A22, A23],
            [A31, A32, A33]
        ]

        st.markdown(
            "<h2 style='text-align:center;'>Result</h2>",
            unsafe_allow_html=True
        )

        st.table(result)


# ---------------------------------------------------------
# SUBTRACTION
# ---------------------------------------------------------

def sub():

    st.markdown(
        "<h2 style='text-align:center;'>Matrix Subtraction</h2>",
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    with col1:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix A</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>[</div>",
            unsafe_allow_html=True
        )

        A = get_matrix("A_sub")

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>]</div>",
            unsafe_allow_html=True
        )

    with op:

        st.markdown(
            "<div style='font-size:45px; text-align:center; padding-top:100px;'>−</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix B</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>[</div>",
            unsafe_allow_html=True
        )

        B = get_matrix("B_sub")

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>]</div>",
            unsafe_allow_html=True
        )

    calculate = st.button(
        "Calculate",
        key="sub_button",
        use_container_width=True
    )

    if calculate:

        A11 = A[0][0] - B[0][0]
        A12 = A[0][1] - B[0][1]
        A13 = A[0][2] - B[0][2]

        A21 = A[1][0] - B[1][0]
        A22 = A[1][1] - B[1][1]
        A23 = A[1][2] - B[1][2]

        A31 = A[2][0] - B[2][0]
        A32 = A[2][1] - B[2][1]
        A33 = A[2][2] - B[2][2]

        result = [
            [A11, A12, A13],
            [A21, A22, A23],
            [A31, A32, A33]
        ]

        st.markdown(
            "<h2 style='text-align:center;'>Result</h2>",
            unsafe_allow_html=True
        )

        st.table(result)


# ---------------------------------------------------------
# MULTIPLICATION
# ---------------------------------------------------------

def mul():

    st.markdown(
        "<h2 style='text-align:center;'>Matrix Multiplication</h2>",
        unsafe_allow_html=True
    )

    col1, op, col2 = st.columns([5, 1, 5])

    with col1:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix A</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>[</div>",
            unsafe_allow_html=True
        )

        A = get_matrix("A_mul")

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>]</div>",
            unsafe_allow_html=True
        )

    with op:

        st.markdown(
            "<div style='font-size:45px; text-align:center; padding-top:100px;'>×</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            "<h3 style='text-align:center;'>Matrix B</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>[</div>",
            unsafe_allow_html=True
        )

        B = get_matrix("B_mul")

        st.markdown(
            "<div style='text-align:center; font-size:70px;'>]</div>",
            unsafe_allow_html=True
        )

    calculate = st.button(
        "Calculate",
        key="mul_button",
        use_container_width=True
    )

    if calculate:

        A11 = (
            A[0][0] * B[0][0]
            + A[0][1] * B[1][0]
            + A[0][2] * B[2][0]
        )

        A12 = (
            A[0][0] * B[0][1]
            + A[0][1] * B[1][1]
            + A[0][2] * B[2][1]
        )

        A13 = (
            A[0][0] * B[0][2]
            + A[0][1] * B[1][2]
            + A[0][2] * B[2][2]
        )

        A21 = (
            A[1][0] * B[0][0]
            + A[1][1] * B[1][0]
            + A[1][2] * B[2][0]
        )

        A22 = (
            A[1][0] * B[0][1]
            + A[1][1] * B[1][1]
            + A[1][2] * B[2][1]
        )

        A23 = (
            A[1][0] * B[0][2]
            + A[1][1] * B[1][2]
            + A[1][2] * B[2][2]
        )

        A31 = (
            A[2][0] * B[0][0]
            + A[2][1] * B[1][0]
            + A[2][2] * B[2][0]
        )

        A32 = (
            A[2][0] * B[0][1]
            + A[2][1] * B[1][1]
            + A[2][2] * B[2][1]
        )

        A33 = (
            A[2][0] * B[0][2]
            + A[2][1] * B[1][2]
            + A[2][2] * B[2][2]
        )

        result = [
            [A11, A12, A13],
            [A21, A22, A23],
            [A31, A32, A33]
        ]

        st.markdown(
            "<h2 style='text-align:center;'>Result</h2>",
            unsafe_allow_html=True
        )

        st.table(result)


# ---------------------------------------------------------
# DETERMINANT
# ---------------------------------------------------------

def det():

    st.markdown(
        "<h2 style='text-align:center;'>Determinant</h2>",
        unsafe_allow_html=True
    )

    st.markdown
