
WELCOME_MESSAGE = """
     **xin chao!!**
               __   __
              __ \\ / __
             /  \\ | /  \\
                 \\|/
            _,.---v---._
   /\\__/\\  /            \\
   \\_  _/ /              \\
     \\ \\_|           @ __|
      \\                \\_
       \\     ,__/       /
     ~~~`~~~~~~~~~~~~~~/~~~~
"""

WARNING_MESSAGE = """
         ______________________
        |                      |
        | CANH BAO NGUY HIEM!! |
        |______________________|
                                  /^^^/           /]
                                 /   ]           / ]
      O                  _______/    ]___       /  ]
                        /                \\_____/   /
   O                  _/   [@]  \\ \\                \\
           ___//_    /..         | |                ]
    o     /o )   \\/   VVVvvv\    | |         _/\\    ]
      O<  )___\\\\_/\\         |               /    \\  ]
                     AAA^^^^^              /       \\]
                      \\_________\\   \\_____/
                               \\    \\
                                \\____\\
"""

print("Mật khẩu để mở cửa ")
matkhau = 1234
dem = 0
while True:
    Pass = int(input("Nhập mật khẩu của bạn"))
    if Pass != matkhau:
        dem = dem + 1
        print("cửa không mở")
    else:
        print(WELCOME_MESSAGE)
        break
    if dem == 3:
        print(WARNING_MESSAGE)
        break
