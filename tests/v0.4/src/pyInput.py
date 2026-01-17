# from pynput import keyboard
#
# def get_input():
#     choice = None
#
#     def on_press(key):
#         nonlocal choice
#
#         try:
#             choice = key
#             return False  # stop listener
#         except Exception as e:
#             print(e)
#
#     with keyboard.Listener(on_press=on_press) as listener:
#         listener.join()
#
#     return choice
#
# i = get_input()
# print("\n"+i.char)