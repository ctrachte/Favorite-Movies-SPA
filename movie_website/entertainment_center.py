import media

movies = {'movie1':{'title':"Blade Runner",
	'plot_summary':"Deckard (Harrison Ford) is forced by the police Boss (M. Emmet Walsh) to continue his old job as Replicant Hunter. His assignment: eliminate four escaped Replicants from the colonies who have returned to Earth. Before starting the job, Deckard goes to the Tyrell Corporation and he meets Rachel (Sean Young), a Replicant girl he falls in love with.",
	'poster_image':"http://t3.gstatic.com/images?q=tbn:ANd9GcTcvek3p12Gwqwk-2wjTSHWTNq0LTTeoOgXUwqerVOY2u9zjOgO",
	'trailer':"https://www.youtube.com/watch?v=eogpIG53Cis"}}

blade_runner = media.Movie(movies['movie1']['title'], movies['movie1']['plot_summary'],movies['movie1']['poster_image'],movies['movie1']['trailer'])

print (blade_runner.storyline)