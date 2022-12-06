class Title:
    all_titles = ["test1","test2"]
    def missingTitle(new_list:list, max_list:list) -> list:
        filled_list=new_list
        for name in max_list:
            if name not in new_list:filled_list.append(name)
            else:pass
        return filled_list