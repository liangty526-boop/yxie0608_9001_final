from jianbing_robot import JianBingOrder

def display_welcome():
    
    print("\n     Welcome to Jianbing Master!")
    print("*"*40)
    print("\n1. Start Order")
    print("2. Exit\n")
    print("*"*40)

def main():
    while True:
        
        display_welcome()
        user_input = input("Please enter your choice (1 or 2): ").strip()
        
        if user_input == "1":
            # 实例化订单类
            order = JianBingOrder()
            # 开始定制
            order.start_customization()
            # 打印小票
            order.print_receipt()
            # 展示煎饼图片
            order.show_final_image()
            
            input("\nPress Enter to return to the main menu...")
            
        elif user_input == "2":
            print("\nThank you for using our Jianbing Master! SEE YOU")
            break
        else:
            print("\n Invalid input! Please enter the number 1 or 2.")

if __name__ == "__main__":
    main()