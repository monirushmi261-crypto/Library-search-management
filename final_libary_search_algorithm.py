"""
Library Book Search Management System
--------------------------------------
Data Structures Assignment - Streamlit Web Application

Data Structure Used : List of Dictionaries
Search Technique     : Linear Search (case-insensitive)

Author : Steffi
"""

import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Library Book Search Management",
    page_icon="📚",
    layout="centered"
)

# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================
# The book database is stored as a LIST OF DICTIONARIES.
# Each dictionary represents one book record:
#   { "id": int, "title": str, "author": str, "genre": str }
if "books" not in st.session_state:
    st.session_state.books = []

# Auto-incrementing ID counter (kept separate so IDs never repeat,
# even after later deletions in an extended version of this app)
if "next_id" not in st.session_state:
    st.session_state.next_id = 1


# ============================================================
# MODULE 1: ADD BOOK
# ============================================================
def add_book(title: str, author: str, genre: str) -> dict:
    """
    Adds a new book record to the in-memory book list.

    Parameters
    ----------
    title, author, genre : str

    Returns
    -------
    dict : the newly created book record
    """
    new_book = {
        "id": st.session_state.next_id,
        "title": title.strip(),
        "author": author.strip(),
        "genre": genre.strip() if genre.strip() else "General",
    }
    st.session_state.books.append(new_book)
    st.session_state.next_id += 1
    return new_book


# ============================================================
# MODULE 2: DISPLAY BOOKS
# ============================================================
def display_books() -> list:
    """
    Returns the full list of book records for display.
    Kept as its own function (instead of inlining) to satisfy the
    'modular function' rubric requirement and to make the data
    source swappable later (e.g. reading from a file/DB).
    """
    return st.session_state.books


# ============================================================
# MODULE 3: SEARCH BOOK (Linear Search)
# ============================================================
def search_book(query: str, search_by: str) -> list:
    """
    Performs a case-insensitive LINEAR SEARCH over the book list.

    Parameters
    ----------
    query : str
        The search term entered by the user.
    search_by : str
        One of "ID", "Title", "Author", "Genre".

    Returns
    -------
    list : all matching book records (empty list if none found)

    Time Complexity  : O(n)  -> every record is checked once in the
                                 worst case (n = number of books)
    Space Complexity : O(k)  -> k = number of matches returned
    """
    results = []
    query_clean = query.strip().lower()

    for book in st.session_state.books:               # linear scan, O(n)
        if search_by == "ID":
            # Allow partial / exact numeric match safely
            if query_clean.isdigit() and book["id"] == int(query_clean):
                results.append(book)
        elif search_by == "Title":
            if query_clean in book["title"].lower():
                results.append(book)
        elif search_by == "Author":
            if query_clean in book["author"].lower():
                results.append(book)
        elif search_by == "Genre":
            if query_clean in book["genre"].lower():
                results.append(book)

    return results


# ============================================================
# UI HELPER: render a single book nicely (used by search results)
# ============================================================
def render_book_card(book: dict):
    st.markdown(
        f"""
        **📖 {book['title']}**
        &nbsp;&nbsp;·&nbsp;&nbsp; ID: `{book['id']}`

        - ✍️ **Author:** {book['author']}
        - 🏷️ **Genre:** {book['genre']}
        """
    )
    st.divider()


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
st.sidebar.title("📚 Library Menu")
page = st.sidebar.radio(
    "Navigate to:",
    ["➕ Add Book", "📋 Display Books", "🔍 Search Book"]
)

st.sidebar.markdown("---")
# Placeholder created here (so it stays in this visual position),
# but the actual value is written at the END of the script (see
# bottom of file) - this guarantees it reflects the state AFTER
# any add/search action that happened during this run, not before.
book_count_placeholder = st.sidebar.empty()

# ============================================================
# PAGE: ADD BOOK
# ============================================================
if page == "➕ Add Book":
    st.title("📚 Library Book Search Management")
    st.subheader("➕ Add a New Book")

    # clear_on_submit=True resets all widgets inside the form
    # automatically after a successful submission - no manual
    # session_state clearing needed (avoids the classic
    # "cannot modify widget key after instantiation" error).
    with st.form("add_book_form", clear_on_submit=True):
        title = st.text_input("Book Title *")
        author = st.text_input("Author Name *")
        genre = st.text_input("Genre (optional)")

        submitted = st.form_submit_button("Add Book ➕")

        if submitted:
            if not title.strip() or not author.strip():
                st.error("⚠️ Title and Author are required fields.")
            else:
                book = add_book(title, author, genre)
                st.success(
                    f"✅ '{book['title']}' by {book['author']} "
                    f"added successfully! (Book ID: {book['id']})"
                )

# ============================================================
# PAGE: DISPLAY BOOKS
# ============================================================
elif page == "📋 Display Books":
    st.title("📚 Library Book Search Management")
    st.subheader("📋 All Books in Library")

    books = display_books()

    if not books:
        st.info("ℹ️ No books added yet. Go to **Add Book** to get started.")
    else:
        # Show as a clean table
        table_data = [
            {
                "ID": b["id"],
                "Title": b["title"],
                "Author": b["author"],
                "Genre": b["genre"],
            }
            for b in books
        ]
        st.dataframe(table_data, use_container_width=True, hide_index=True)
        st.caption(f"Total records: {len(books)}")

# ============================================================
# PAGE: SEARCH BOOK
# ============================================================
elif page == "🔍 Search Book":
    st.title("📚 Library Book Search Management")
    st.subheader("🔍 Search for a Book")

    with st.form("search_form"):
        search_by = st.selectbox("Search by", ["Title", "Author", "Genre", "ID"])

        # IMPORTANT: label/key must stay CONSTANT regardless of search_by.
        # If the label changed with search_by (e.g. f"Enter {search_by}..."),
        # Streamlit would treat it as a brand-new widget every time the
        # dropdown changes, silently dropping whatever the user typed on
        # that run (the classic "works on the 2nd click" bug).
        query = st.text_input("Enter your search term", key="search_query")

        # form_submit_button lets the user press Enter to search
        search_clicked = st.form_submit_button("Search 🔍")

    if search_clicked:
        if not query.strip():
            st.error("⚠️ Please enter a value to search.")
        elif not st.session_state.books:
            st.warning("📭 The library is empty. Add some books first.")
        else:
            results = search_book(query, search_by)
            if results:
                st.success(f"✅ Found {len(results)} matching book(s):")
                for book in results:
                    render_book_card(book)
            else:
                st.error(f"❌ No book found matching {search_by} = '{query}'.")

# ============================================================
# FOOTER (also finalizes the sidebar book-count placeholder,
# now that any add/search action for this run has completed)
# ============================================================
book_count_placeholder.metric("Total Books in Library", len(st.session_state.books))
st.sidebar.markdown("---")

