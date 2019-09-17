import LAT
import media

matrix = media.Movie(movie_title = "NARCOS MEXICO",
					 movie_storyline = "Neo searches for the truth about the Matrix and discovers his place in it.", 
					 poster_image = "https://upload.wikimedia.org/wikipedia/en/4/42/Narcos%2C_Mexico_-_Title_card.png", 
					 trailer_youtube = "https://www.youtube.com/watch?v=VBLcYJ7C4F0")

point_break = media.Movie(movie_title = "13 REASONS WHY",
					     movie_storyline = "Reeves stars as rookie FBI agent Johnny Utah, who is investigating a string of bank robberies possibly being committed by surfers. Johnny goes undercover to infiltrate the surfing community and develops a complex friendship with Bodhi (Swayze), the charismatic leader of a gang of surfers.", 
					     poster_image = "https://upload.wikimedia.org/wikipedia/en/7/73/Netflix%27s_13_Reasons_Why_title_screen.png", 
					     trailer_youtube = "https://www.youtube.com/watch?v=Pws-LN_-riM")

fight_club = media.Movie(movie_title = "BLACK MIRROR:SEASON 5",
					     movie_storyline = "An insomniac office worker looking for a way to change his life crosses paths with a devil-may-care soap maker and they form an underground fight club that evolves into something much, much more...", 
					     poster_image = "https://upload.wikimedia.org/wikipedia/en/2/24/BlackMirrorTitleCard.jpg", 
					     trailer_youtube = "https://www.youtube.com/watch?v=2bVik34nWws")

usual_suspects = media.Movie(movie_title = "IT CHAPTER:2",
						     movie_storyline = "A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.", 
						     poster_image = "https://upload.wikimedia.org/wikipedia/en/8/88/ItChapterTwoTeaser.jpg", 
						     trailer_youtube = "https://www.youtube.com/watch?v=xhJ5P7Up3jA")

apollo = media.Movie(movie_title = "JOKER : 2019",
					 movie_storyline = "The film depicts astronauts Lovell, Jack Swigert and Fred Haise aboard Apollo 13 for America's third Moon landing mission. En route, an on-board explosion deprives their spacecraft of most of its oxygen supply and electric power, forcing NASA's flight controllers to abort the Moon landing, and turning the mission into a struggle to get the three men home safely.", 
					 poster_image = "https://en.wikipedia.org/wiki/Joker_(2019_film)#/media/File:Joker_(2019_film)_poster.jpg", 
					 trailer_youtube = "https://www.youtube.com/watch?v=t433PEQGErc")

contact = media.Movie(movie_title = "FAST N FURIOUS:HOBBS & SHAW",
					  movie_storyline = "A SETI scientist who finds strong evidence of extraterrestrial life and is chosen to make first contact.", 
					  poster_image = "https://upload.wikimedia.org/wikipedia/en/0/00/Fast_%26_Furious_Presents_Hobbs_%26_Shaw_-_theatrical_poster.jpg", 
					  trailer_youtube = "https://www.youtube.com/watch?v=HZ7PAyCDwEg")


movies = [matrix, point_break, fight_club, usual_suspects, apollo, contact]
fresh_tomatoes.open_movies_page(movies)