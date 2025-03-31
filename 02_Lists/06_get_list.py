def get_list(list):
    print(list)

    def main():
        num_list=[]

        element=input("Enter your Numbers you want to save in a List")

        while element != "":
            num_list.appent(int(element))
            element=input("enter the numbers you want to save in a list or press enter to stop ")

            get_list(num_list)

        if __name__ == "__main__":
            main()