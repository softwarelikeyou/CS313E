def makeBalls(game):
    balls = []
    for index, ball in enumerate(game):
        if ball == '-':
            ball = 0
        if ball == 'X':
            ball = 10
        if ball == '/':
            if game[index-1] == '-':
                ball = 10
            else:
                ball = 10 - int(game[index-1])
                    
        balls.append(int(ball))
    return balls

def makeFrames(game):
    #   X    9  /    X    9  /    X    9 /    X     9   /    X     9   /    X
    # [[0], [1, 2], [3], [4, 5], [6], [7, 8], [9], [10, 11], [12], [13, 14, 15]]
    # [[0], [1, 2], [3], [4, 5], [6], [7, 8], [9], [10, 11], [12], [13, 14, 15]]
    frames = []
    frame = []
    ballcount = 0
    framecount = 0
    for index, ball in enumerate(game):
        if framecount == 9:
            for k in range(index, len(game)):
                frame.append(k)
            frames.append(frame)
            break
        
        if ball == 'X':
            frame.append(index)
            frames.append(frame)
            framecount += 1
            frame = []
            ballcount = 0

        else:
            frame.append(index)
            ballcount += 1
            if (ballcount == 2):
                frames.append(frame)
                framecount += 1
                frame = []
                ballcount = 0
            
    return frames

def makeFramesInput(game):
    frames = []
    frame = []
    ballcount = 0
    framecount = 0
    for index, ball in enumerate(game):
        if framecount == 9:
            for k in range(index, len(game)):
                frame.append(game[k])
            frames.append(frame)
            break
        
        if ball == 'X':
            frame.append(ball)
            frames.append(frame)
            framecount += 1
            frame = []
            ballcount = 0

        else:
            frame.append(ball)
            ballcount += 1
            if (ballcount == 2):
                frames.append(frame)
                framecount += 1
                frame = []
                ballcount = 0
            
    return frames

def makeScore(balls, frames):
    scores = [0,0,0,0,0,0,0,0,0,0]
    for index, frame in enumerate(frames):
        if len(frame) == 1:
            if len(frames[index + 1]) == 1:
                scores[index] += 10 + balls[frame[0]+1] + balls[frame[0]+2]
            elif len(frames[index + 1]) == 2:
                scores[index] += 10 + balls[frame[0]+1] + balls[frame[0]+2]
            elif len(frames[index + 1]) == 3:
                scores[index] += 10 + balls[frame[0]+1] + balls[frame[0]+2]

            if (index > 0):
                scores[index] += scores[index-1]

        if len(frame) == 2:
            if balls[frame[0]] + balls[frame[1]] == 10:
                scores[index] += 10 + balls[frame[1]+1]
            else:
                scores[index] += balls[frame[0]] + balls[frame[1]]

            if (index > 0):
                scores[index] += scores[index-1]
            
        if len(frame) == 3:
            if balls[frame[0]] == 10:
                scores[index] += balls[frame[0]] + balls[frame[1]] + balls[frame[2]]
            elif balls[frame[0]] + balls[frame[1]] == 10:
                scores[index] += 10 + balls[frame[2]]        
                    
            scores[index] += scores[index-1]

    return scores

def display(balls, frames, scores):
#1   2   3   4   5   6   7   8   9   10   
#+---+---+---+---+---+---+---+---+---+-----+
#|8 /|7 2|9 /|X  |- 7|X  |- -|9 /|X  |X 9 /!
#| 17| 26| 46| 63| 70| 80| 80|100|129|  149!
#+---+---+---+---+---+---+---+---+---+-----+    
    print('  ', end="")
    for index, frame in enumerate(frames):
      print(index+1, '  ', end="")
    print("", end="\n")
    
    for index, frame in enumerate(frames):
      print('+---', end="")
    print('--+', end="\n")
    
    for index, frame in enumerate(frames):
        if len(frame) == 1:
            print("|{0:>3}".format(frame[0]), end="")           
        elif len(frame) == 2 and index != 9:
            print("|{0} {1}".format(frame[0], frame[1]), end="")
        elif len(frame) == 2 and index == 9:
            print("|{0} {1} {2}".format(frame[0], frame[1], " "), end="")            
        elif len(frame) == 3:
            print("|{0} {1} {2}".format(frame[0], frame[1], frame[2]), end="")
    print("|{:>3}".format(""),end="\n")
    
    for index, score in enumerate(scores):
      if index == 9:
        print("|{:>5}".format(score),end="")
      else:
        print("|{:>3}".format(score),end="")
    print("|",end="\n")
    
    for index, frame in enumerate(frames):
      print('+---', end="")
    print('--+', end="\n\n")
    
def main():
    games = open("scores.txt", 'r')
    balls = []
    frames = []
    scores = []
    for game in games:
        game.strip()
        #         X   X   X   X   X   X   X   X   X   X   X   X = 300
        #balls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        #frames = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9, 10, 11]]

        # Tested
        #         -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - = 0
        #balls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #frames = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        # Tested
        #         8  1  8  1  8  1  8  1  8  1  8  1  8  1  8  1  8  1  8  1 = 90
        #balls = [8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1]
        #frames = [[8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1]]

        # Tested
        #         -  /  1  /  2  /  3  /  4  /  5  /  6  /  7  /  8  /  9  /   X = 155
        #balls = [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 10]
        #frames = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19, 20]]

        # Tested
        #       6  2  8  /  9  /   X   X   X   X  8  /   X  9  /  8 = 213
        #balls = [6, 2, 8, 2, 9, 1, 10, 10, 10, 10, 8, 2, 10, 9, 1, 8]
        #frames = [[0, 1], [2,3], [4,5], [6], [7], [8], [9], [10, 11], [12], [13, 14, 15]]

        # Tested
        #         X   X   X   X   X  9  /  7  /   X  7  /   X   X  9 = 245
        #balls = [10, 10, 10, 10, 10, 9, 1, 7, 3, 10, 7, 3, 10, 10, 9]
        #frames = [[0], [1], [2], [3], [4], [5, 6], [7, 8], [9], [10, 11], [12, 13, 14]]

        # Tested
        #         9, -, 8, 1, 7, 2,  X,  X, 9, -,  X,  X,  X, 8, 1 = 170
        #balls = [9, 0, 8, 1, 7, 2, 10, 10, 9, 0, 10, 10, 10, 8, 1]
        #frames = [[0, 1], [2, 3], [4, 5], [6], [7], [8, 9], [10], [11], [12], [13, 14]]

        # Tested
        #         X  9  /   X  9  /   X  9  /   X  9  /   X  9  /   X = 200
        #balls = [10, 9, 1, 10, 9, 1, 10, 9, 1, 10, 9, 1, 10, 9, 1, 10]
        #frames = [[0], [1, 2], [3], [4, 5], [6], [7,8], [9], [10, 11], [12], [13, 14, 15]]

        # Tested
        #        8  /  7  2  9  /   X  -  7   X  -  -  9  /   X   X  9  / = 149
        #balls = [8, 2, 7, 2, 9, 1, 10, 0, 7, 10, 0, 0, 9, 1, 10, 10, 9, 1]
        #frames = [[0,1], [2, 3], [4, 5], [6], [7, 8], [9], [10, 11], [12, 13], [14], [15, 16, 17]]
        
        balls = makeBalls(game.split())
        #print(balls)
        frames = makeFrames(game.split())
        #print(frames)
        scores = makeScore(balls, frames)
        raw = makeFramesInput(game.split())
        #print(raw)
        #print(scores)
        display(balls, raw, scores)
main()
