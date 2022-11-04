import view as vie
import controller as contrl


n_o = vie.hello_one()
n_tw = vie.hello_two()


gst = contrl.game_start(name_one_player=n_o, name_two_player=n_tw, matrix_game=vie.playing_field())
vie.winner(count=gst[0], random_move=gst[1], name_one_player=n_o, name_two_player=n_tw)
