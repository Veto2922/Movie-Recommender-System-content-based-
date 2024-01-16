import streamlit as st
import pandas as pd
from src.models.predict_model import get_top_n_movies, recommmendation_by_id

# Get top 20 movies
top_movies_df = get_top_n_movies(n=30)

def main():
    st.set_page_config(layout="wide")
    # Streamlit App
    st.markdown(
        """
        <h1 style='text-align: center; color: blue;'>🎬 Movie Recommendation System</h1>
        """,
        unsafe_allow_html=True
    )
    st.info('This project suggests to you the most famous films on the home page, and when you click on the name of the film, it shows you the films most similar to this film.')
    
    # st.title('🎬 Movie Recommendation System')
    st.markdown("---")

    # Display movie posters in rows and columns with movie details
    st.title('Top Movies')
    num_columns = 6  # Number of columns for the posters

    # Split the screen into columns
    columns = st.columns(num_columns)

    for index, row in get_top_n_movies(n=20).iterrows():
        # Display movie poster in the current column
        with columns[index % num_columns]:
            # Display movie details underneath the poster
            st.image(row['movie_poster'], caption=row['title'], use_column_width=True)
            st.write(f"**Release Year:** {row['release_year']}")
            st.write(f"**Runtime:** {row['runtime']} minutes")
            st.write(f"**Vote Average:** {row['vote_average']}")
            # Button-like behavior on clicking the image
            if st.button(row['title'], key=f"button_{index}"):
                selected_movie_id = row['movie_id']
                recommendations = recommmendation_by_id(selected_movie_id)

                if recommendations is not None:
                    st.sidebar.title(f":red[Movies similar to {row['title']} :] ")
                    for rec_index, rec_row in recommendations.iterrows():
                        # Display movie poster in the sidebar
                        st.sidebar.image(rec_row['movie_poster'], caption=rec_row['title'], use_column_width=True)

                        # Display movie details underneath the poster in the sidebar
                        st.sidebar.markdown(f"**Title:** {rec_row['title']}")
                        st.sidebar.markdown(f"**Release Year:** {rec_row['release_year']}")
                        st.sidebar.markdown(f"**Runtime:** {rec_row['runtime']} minutes")
                        st.sidebar.markdown(f"**Vote Average:** {rec_row['vote_average']}")
                        st.sidebar.markdown("---")

                else:
                    st.warning('Invalid Movie ID. Please enter a valid Movie ID.')

    # Add some footer text or additional information
    st.markdown("---")
    st.markdown("Developed by Abdelrahman Mohamed")
        ##############################################################
    # Footer with LinkedIn, GitHub, and Medium links
    st.markdown('---')
    st.subheader('🚀 For more info about this project:')
    st.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdelrahman_Mohamed-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdelrahman-mohamed-28649120b/) [![GitHub](https://img.shields.io/badge/GitHub-Veto2922-darkgreen?style=flat&logo=github)](https://github.com/Veto2922/Movie-Recommender-System-content-based-)')

    if st.button('🚀 Show Support'):
        st.balloons()

    if st.button('🚀 Star on GitHub'):
        st.write('⭐️ Thank you for your support!')



if __name__ == '__main__':
    main()
