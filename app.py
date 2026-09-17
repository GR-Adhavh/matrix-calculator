import streamlit as st


# ---------------------------------------------------------
# Helper function to get a 3x3 matrix
# ---------------------------------------------------------
def get_matrix(prefix):
    matrix = []

    for i in range(3):
        row = []
        for j in range(3):
            value = st.number_input(
                f"{prefix}[{i + 1},{j + 1}]",
                value=0,
                step=1,
                key=f"{prefix}_{i}_{j}"
            )
            row.append(value)
        matrix.append(row)

    return matrix


# ---------------------------------------------------------
# ADDITION
# ---------------------------------------------------------
def add():
    st.subheader("Matrix Addition")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Matrix A")
        A = get_matrix("A_add")

    with col2:
        st.write("Matrix B")
        B = get_matrix("B_add")

    if st.button("Calculate Addition", key="add_button"):

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

        st.write("### Result")
        st.table(result)


# ---------------------------------------------------------
# SUBTRACTION
# ---------------------------------------------------------
def sub():
    st.subheader("Matrix Subtraction")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Matrix A")
        A = get_matrix("A_sub")

    with col2:
        st.write("Matrix B")
        B = get_matrix("B_sub")

    if st.button("Calculate Subtraction", key="sub_button"):

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

        st.write("### Result")
        st.table(result)


# ---------------------------------------------------------
# MULTIPLICATION
# ---------------------------------------------------------
def mul():
    st.subheader("Matrix Multiplication")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Matrix A")
        A = get_matrix("A_mul")

    with col2:
        st.write("Matrix B")
        B = get_matrix("B_mul")

    if st.button("Calculate Multiplication", key="mul_button"):

        A11 = (A[0][0] * B[0][0]) + \
              (A[0][1] * B[1][0]) + \
              (A[0][2] * B[2][0])

        A12 = (A[0][0] * B[0][1]) + \
              (A[0][1] * B[1][1]) + \
              (A[0][2] * B[2][1])

        A13 = (A[0][0] * B[0][2]) + \
              (A[0][1] * B[1][2]) + \
              (A[0][2] * B[2][2])

        A21 = (A[1][0] * B[0][0]) + \
              (A[1][1] * B[1][0]) + \
              (A[1][2] * B[2][0])

        A22 = (A[1][0] * B[0][1]) + \
              (A[1][1] * B[1][1]) + \
              (A[1][2] * B[2][1])

        A23 = (A[1][0] * B[0][2]) + \
              (A[1][1] * B[1][2]) + \
              (A[1][2] * B[2][2])

        A31 = (A[2][0] * B[0][0]) + \
              (A[2][1] * B[1][0]) + \
              (A[2][2] * B[2][0])

        A32 = (A[2][0] * B[0][1]) + \
              (A[2][1] * B[1][1]) + \
              (A[2][2] * B[2][1])

        A33 = (A[2][0] * B[0][2]) + \
              (A[2][1] * B[1][2]) + \
              (A[2][2] * B[2][2])

        result = [
            [A11, A12, A13],
            [A21, A22, A23],
            [A31, A32, A33]
        ]

        st.write("### Result")
        st.table(result)


# ---------------------------------------------------------
# DETERMINANT
# ---------------------------------------------------------
def det():
    st.subheader("3 × 3 Matrix Determinant")

    A = get_matrix("A_det")

    if st.button("Calculate Determinant", key="det_button"):

        a11 = A[0][0]
        a12 = A[0][1]
        a13 = A[0][2]

        a21 = A[1][0]
        a22 = A[1][1]
        a23 = A[1][2]

        a31 = A[2][0]
        a32 = A[2][1]
        a33 = A[2][2]

        D = (
            a11 * ((a22 * a33) - (a23 * a32))
            - a12 * ((a21 * a33) - (a23 * a31))
            + a13 * ((a21 * a32) - (a22 * a31))
        )

        st.success(f"Determinant = {D}")


# ---------------------------------------------------------
# INVERSE
# ---------------------------------------------------------
def inv():
    st.subheader("3 × 3 Matrix Inverse")

    A = get_matrix("A_inv")

    if st.button("Calculate Inverse", key="inv_button"):

        a11 = A[0][0]
        a12 = A[0][1]
        a13 = A[0][2]

        a21 = A[1][0]
        a22 = A[1][1]
        a23 = A[1][2]

        a31 = A[2][0]
        a32 = A[2][1]
        a33 = A[2][2]

        # Determinant
        D = (
            a11 * ((a22 * a33) - (a23 * a32))
            - a12 * ((a21 * a33) - (a23 * a31))
            + a13 * ((a21 * a32) - (a22 * a31))
        )

        if D == 0:
            st.warning("Inverse does not exist because determinant is 0.")

        else:

            A11 = (a22 * a33 - a23 * a32) / D
            A12 = -((a12 * a33) - (a13 * a32)) / D
            A13 = (a12 * a23 - a13 * a22) / D

            A21 = -((a21 * a33) - (a23 * a31)) / D
            A22 = (a11 * a33 - a13 * a31) / D
            A23 = -((a11 * a23) - (a13 * a21)) / D

            A31 = (a21 * a32 - a22 * a31) / D
            A32 = -((a11 * a32) - (a12 * a31)) / D
            A33 = (a11 * a22 - a12 * a21) / D

            result = [
                [A11, A12, A13],
                [A21, A22, A23],
                [A31, A32, A33]
            ]

            st.write("### Inverse")
            st.table(result)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
def main():

    st.set_page_config(
        page_title="Matrix Calculator",
        page_icon="🔢",
        layout="centered"
    )

    st.title("🔢 3 × 3 Matrix Calculator")
    st.write("Perform matrix addition, subtraction, multiplication, determinant and inverse.")

    operation = st.sidebar.selectbox(
        "Select Operation",
        [
            "Add",
            "Subtract",
            "Multiply",
            "Determinant",
            "Inverse"
        ]
    )

    if operation == "Add":
        add()

    elif operation == "Subtract":
        sub()

    elif operation == "Multiply":
        mul()

    elif operation == "Determinant":
        det()

    elif operation == "Inverse":
        inv()


if __name__ == "__main__":
    main()