import fresh_tomatoes
import media

movies = {'movie1':{'title':"Blade Runner",
	'plot_summary':"Deckard (Harrison Ford) is forced by the police Boss (M. Emmet Walsh) to continue his old job as Replicant Hunter. His assignment: eliminate four escaped Replicants from the colonies who have returned to Earth. Before starting the job, Deckard goes to the Tyrell Corporation and he meets Rachel (Sean Young), a Replicant girl he falls in love with.",
	'poster_image':"http://t3.gstatic.com/images?q=tbn:ANd9GcTcvek3p12Gwqwk-2wjTSHWTNq0LTTeoOgXUwqerVOY2u9zjOgO",
	'trailer':"https://www.youtube.com/watch?v=eogpIG53Cis"},

	'movie2':{'title':"Ghost in the Shell 1995",
	'plot_summary':"In this Japanese animation, cyborg federal agent Maj. Motoko Kusanagi (Mimi Woods) trails 'The Puppet Master' (Abe Lasser), who illegally hacks into the computerized minds of cyborg-human hybrids. Her pursuit of a man who can modify the identity of strangers leaves Motoko pondering her own makeup and what life might be like if she had more human traits. With her partner (Richard George), she corners the hacker, but her curiosity about her identity sends the case in an unforeseen direction.",
	'poster_image':"http://t2.gstatic.com/images?q=tbn:ANd9GcSRHINQm1r493AJQIMk9J2CMtl5AbO5IgyTGmQV64FQbxXO8AwU",
	'trailer':"https://www.youtube.com/watch?v=p2MEaROKjaE"},

	'movie3':{'title':"Blade Runner 2049",
	'plot_summary':"Officer K (Ryan Gosling), a new blade runner for the Los Angeles Police Department, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. His discovery leads him on a quest to find Rick Deckard (Harrison Ford), a former blade runner who's been missing for 30 years.",
	'poster_image':"https://pbs.twimg.com/media/DH9QvgAUQAAZANa.jpg:large",
	'trailer':"https://www.youtube.com/watch?v=gCcx85zbxz4"},

	'movie4':{'title':"Prometheus",
	'plot_summary':"The discovery of a clue to mankind's origins on Earth leads a team of explorers to the darkest parts of the universe. Two brilliant young scientists lead the expedition. Shaw (Noomi Rapace) hopes that they will meet a race of benevolent, godlike beings who will in some way verify her religious beliefs, while Holloway (Logan Marshall-Green) is out to debunk any spiritual notions. However, neither the scientists nor their shipmates are prepared for the unimaginable terrors that await them.",
	'poster_image':"http://t1.gstatic.com/images?q=tbn:ANd9GcR3blsaJx2hxJPhPCfLJA3knB4T8FUJtrvG-EIF9BTmtbIvXy02",
	'trailer':"https://www.youtube.com/watch?v=34cEo0VhfGE"},

	'movie5':{'title':"Hot Rod",
	'plot_summary':"For Rod Kimball (Andy Samberg), performing stunts is a way of life, even though he is rather accident-prone. Poor Rod cannot even get any respect from his stepfather, Frank (Ian McShane), who beats him up in weekly sparring matches. When Frank falls ill, Rod devises his most outrageous stunt yet to raise money for Frank's operation -- and then Rod will kick Frank's butt.",
	'poster_image':"http://www.gstatic.com/tv/thumb/movieposters/165093/p165093_p_v8_aa.jpg",
	'trailer':"https://www.youtube.com/watch?v=DhdrA9qz79o"}
	}

blade_runner = media.Movie(movies['movie1']['title'], movies['movie1']['plot_summary'],movies['movie1']['poster_image'],movies['movie1']['trailer'])

gits_1995 = media.Movie(movies['movie2']['title'], movies['movie2']['plot_summary'],movies['movie2']['poster_image'],movies['movie2']['trailer'])

blade_runner_2049 = media.Movie(movies['movie3']['title'], movies['movie3']['plot_summary'],movies['movie3']['poster_image'],movies['movie3']['trailer'])

prometheus = media.Movie(movies['movie4']['title'], movies['movie4']['plot_summary'],movies['movie4']['poster_image'],movies['movie4']['trailer'])

hot_rod = media.Movie(movies['movie5']['title'], movies['movie5']['plot_summary'],movies['movie5']['poster_image'],movies['movie5']['trailer'])

movie_ids = [blade_runner,gits_1995,blade_runner_2049,prometheus,hot_rod]

fresh_tomatoes.open_movies_page(movie_ids)

#print (blade_runner.storyline)
#blade_runner.show_trailer()