import ingredients

class JianBingOrder:
    def __init__(self):
        self.total_price = ingredients.base_price
        self.selected_ingredients = []

    def get_choice(self, category_name, options, allow_multiple = False):
        while True:
            print(f'\n Please choose your {category_name}')
            for key,(name, price) in options.items():
                print(f'[{key}] {name}(+${price:.2f})')
            print("\nTip: If you don't know what the option is, you can enter ? View details")

            user_input = input('Please select the number: ').strip()

            #?
            if user_input == '?':
                print(f'\nSearching for the detailed diagram of [{category_name}] for you...')
                try:
                    with open(f'{category_name}.txt','r', encoding='utf-8') as f:
                        print(f.read())
                except FileNotFoundError:
                    print(f'Sorry, the detailed file of [{category_name}.txt] was not found for the time being.')
                continue
        
            try:
                choice = int(user_input)
                if choice not in options:
                    print('Input error! The serial number is not in the option, please select it again.')
                    continue

                #多选
                if allow_multiple and choice == 0 :
                    break
                #获取配料和价格
                name, price = options[choice]

                #记录
                self.selected_ingredients.append(name)
                self.total_price += price
                print('\n\n\n'+"*"*40)
                print(f'Successfully selected {name}(+${price:.2f})')

                #不是多选
                if not allow_multiple:
                    break
                else:
                    print('\nTip: You can add more items, or enter 0 to move on to the next section. ')
            except:
                print('Input error! Please enter the number, or enter ? to view details')

    def start_customization(self):
        print("\n Start to customize your jianbing......")
        
        # 1. 鸡蛋（单选）
        self.get_choice("egg", ingredients.egg_options, allow_multiple=False)
        # 2. 酱料（单选）
        self.get_choice("sauce", ingredients.sauce_options, allow_multiple=False)
        # 3. 脆（单选）
        self.get_choice("crispy", ingredients.crispy_options, allow_multiple=False)
        
        # 4. 肉类（多选，直到按0退出）
        self.get_choice("meat", ingredients.meat_options, allow_multiple=True)
        # 5. 蔬菜（多选）
        self.get_choice("vegetable", ingredients.vegetable_options, allow_multiple=True)
        # 6. 小料（多选）
        self.get_choice("seasoning", ingredients.seasoning_options, allow_multiple=True)

    def print_receipt(self):
        print("\n" + "="*30)
        print("   Jianbing Master Receipt   ")
        print("="*30)
        print(f"Base Crepe: ${ingredients.base_price:.2f}")
        print("Added Toppings:")
        if not self.selected_ingredients:
            print("  - No Extra Toppings")
        else:
            for item in self.selected_ingredients:
                print(f"  - {item}")
        print("-"*30)
        print(f"Total Price: ${self.total_price:.2f}")
        print("Thank you for using Jianbing Master!")
        print("="*30)

    def show_final_image(self):
        print("\n Jianbing is being prepared...... ")
        try:
            with open("final_jianbing.txt", "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("Tip: The final Jianbing file was not found in the folder.。")
            print("(Although there is no picture, your pancakes are ready in heart!)")
