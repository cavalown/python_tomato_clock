import time
import requests


def play_voice(path):
    voice = mp3play.load(path)
    voice.play()


def main():
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'現在時間是：{start_time}，開始工作囉！')
    time.sleep(10)
    break_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'現在時間是：{break_time}，休息五分鐘吧！')
    time.sleep(5)
    main()


if __name__ == '__main__':
    while True:
        ready = input('準備好開始工作了嗎？(yes/no):')
        if ready == 'yes':
            main()
        elif ready == 'no':
            print('好喔！掰掰～')
            break
        else:
            print('不懂你捏！再給你一次機會！')
            continue
