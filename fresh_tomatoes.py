import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            height:450px;
        }
        .movie-tile:hover {
            background-color: #EEE;
        }
        .movie-tile-img:hover, .movie-tile-title:hover
        {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-detail,.movie-comments{
            display:none;
        }
        #selected-movie{
            margin: 20px 0px;
        }
        #header{
            position: absolute;
            text-align: center;
            margin-left: 25%;
            margin-right: 25%;
            left: 0;
            right: 0;
        }
        #home{
            display:none;
        }
        div.picture{
            width:270px;
            height:400px;
            overflow:hidden;
        }
        div.picture > img{
            max-width:100%;
            max-height:100%;
        }
        div.comment-row{
            margin:10px 0px;
            border-bottom-style: ridge;
            border-bottom-left-radius: 3px;
            border-bottom-right-radius: 3px;
            border-bottom-color: #428bca;
            border-bottom-width: 1px;
        }
        .new-comment-button{
            margin:10px 0px;
        }
        span.comment-message{
            float:left;
            word-wrap: break-word;
            word-break: break-all;
        }
        span.comment-time{
            float:right;
            font-size:75%;
        }
        .pictures-row{
            float:left;
            margin:10px;
        }
        .left-arrow,.right-arrow{
            width: 20px;
            overflow: hidden;
        }
        .btn-left,.btn-right{
            margin-top: 150px;
            width: 40px;
            height: 40px;
            position: relative;
        }
        .btn-left
        {
            margin-left: 7px;
            -ms-transform: rotate(-45deg); /* IE 9 */
            -webkit-transform: rotate(-45deg); /* Chrome, Safari, Opera */
            transform: rotate(-45deg);
        }
        .btn-right
        {
            right: 28px;
            -ms-transform: rotate(45deg); /* IE 9 */
            -webkit-transform: rotate(45deg); /* Chrome, Safari, Opera */
            transform: rotate(45deg);
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile-img', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Show movie detail
        // Move movie detail information to the screen, and make it visible
        // Hide other movie tiles. 
        $(document).on('click', '.movie-tile-title', function (event) {
            $(this).addClass('movie-tile-title-passive').removeClass('movie-tile-title');
            $('.movie-tile-title-passive').tooltip("destroy");
            $(this).parent().siblings().hide();
            $('#selected-movie-detail').empty().append($(this).siblings('.movie-detail').show()).show();
            $('#selected-movie-comments').empty().append($(this).siblings('.movie-comments').show()).show();
            $('#home').show();
        });
        // Add new comment
        // Prepend the writen comment to the grid below, and empty the text area
        $(document).on('click','.new-comment-button',function(){
            var commentDate = new Date();
            $(this).parent().parent().children('.submitted-comments').prepend("<div class='row comment-row'><span class='comment-message'>"+$(this).siblings("textarea").val()+"</span><span class='comment-time'> | "+commentDate.toLocaleString()+"</span></div>");
            $(this).siblings("textarea").val("");
        });

        // Back to home
        // Move moive detail information to the movie tile back, and hide it.
        // Show other movie tiles
        $(document).on('click', '#home', function (event) {
            var movie_id = $('#selected-movie-detail').children('div.movie-detail').attr('data-movie-id');
            $('#'+movie_id).children('movie-detail').remove();
            $('#'+movie_id).children('movie-comments').remove();
            $('#'+movie_id).append($('#selected-movie-detail').children('div.movie-detail').hide());
            $('#'+movie_id).append($('#selected-movie-comments').children('div.movie-comments').hide());
            $('#selected-movie-detail').empty().hide();
            $('.movie-tile').show();
            $('#home').hide();
            $('.movie-tile-title-passive').tooltip();
            $('.movie-tile-title-passive').addClass('movie-tile-title').removeClass('movie-tile-title-passive');
        });
        //Movie picture browse buttons left, and right
        $(document).on('click','.btn-left',function(){
          changePicture($(this),-1);
        });
        $(document).on('click','.btn-right',function(){
          changePicture($(this),1);
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $(".movie-tile-img,.movie-tile-title").tooltip();
        });
        //Navigate between movie pictures
        function changePicture($button,change)
        {
            $image = $button.parent().siblings('div.picture').children('img');
            var index = parseInt($image.attr('data-current-image-index')) + change;
            index = ((index + 4) % 4)
            var src = $image.attr('data-image-source-url-'+index);
            $image.attr({
            'src': src,
            'data-current-image-index':index
            });
        }
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a id="home" class="navbar-brand" href="#">Back to Movies</a>
            <a id="header" class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    <!-- Movie Detail Modal -->
        <div id="selected-movie-detail" class="selected-movie col-md-6 col-lg-4 text-center">
        </div>
        <div id="selected-movie-comments" class="selected-movie col-md-6 col-lg-4 text-center">
        <div id="selected-movie-comments" class="selected-movie col-md-6 col-lg-4 text-center">
        </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div id="{movie_id}" class="col-md-6 col-lg-4 movie-tile text-center">
    <img class="movie-tile-img" src="{poster_image_url}" width="220" height="342" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" title="Watch Trailer">
    <h2 class="movie-tile-title"  title="Movie Detail">{movie_title}</h2>
    {movie_detail}
</div>
'''

""" Movie detail html template
    Storyline
    Actors
    Release Date
    Pictures with four different picture urls
    Picture browse buttons
    Comments
    New comment textarea, and button
    Comment list grid
"""
movie_detail = '''
<div class="movie-detail" data-movie-id="{movie_id}">
    <div class="row story-line">
        {storyline}
    </div>
    <div class="row actors">
        Actors: {actors}
    </div>
    <div class="row date">
        Release Date: {release_date}
    </div>
    <div class="pictures row">
        <div class="left-arrow pictures-row">
            <button type="button" class="btn btn-left btn-primary"></button>
        </div>
        <div class="picture pictures-row">
            <img src="{picture_0}" 
            data-current-image-index="0" 
            data-image-source-url-0="{picture_0}" 
            data-image-source-url-1="{picture_1}" 
            data-image-source-url-2="{picture_2}" 
            data-image-source-url-3="{picture_3}" >
        </div>
        <div class="right-arrow pictures-row">
            <button type="button" class="btn btn-right btn-primary"></button>
        </div>
    </div>
</div>  
<div class="movie-comments">
    <div class="new-comment row">
        <textarea class="new-comment-text" cols="50" rows="7" placeholder="Write new comment..."></textarea>
        <button class="new-comment-button btn btn-primary" type="button" class="btn btn-primary">Add Comment</button>
    </div>
    <div class="submitted-comments"></div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        
        content_detail = movie_detail.format(
            movie_id=movie.movie_id,
            storyline=movie.storyline,
            actors=','.join(movie.actors),
            release_date=movie.release_date,
            picture_0=movie.picture[0],
            picture_1=movie.picture[1],
            picture_2=movie.picture[2],
            picture_3=movie.picture[3],
            trailer_youtube_id=trailer_youtube_id
        )
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_id=movie.movie_id,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_detail=content_detail
        )
        print(movie.movie_id)
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
