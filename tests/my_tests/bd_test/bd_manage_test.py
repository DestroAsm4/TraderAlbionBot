from bd.manage_bd import ManageBD

manage_bd = ManageBD("t_bd")

def create_all_t():
    manage_bd.create("buy_mail")
    manage_bd.create("sell_mail")
    manage_bd.create("order_sell")
    manage_bd.create("not_valid")
    manage_bd.create("valid_data")

def create_one_t(name):
    manage_bd.create(name)



def delete_all_table_t():
    '''
    'buy_mail', 'sell_mail', 'order_sell', 'not_valid', 'valid_data'
    '''
    manage_bd.del_table("buy_mail")
    manage_bd.del_table("sell_mail")
    manage_bd.del_table("order_sell")
    manage_bd.del_table("not_valid")
    manage_bd.del_table("valid_data")

def delete_one_table_t(name):
    '''
    'buy_mail', 'sell_mail', 'order_sell', 'not_valid', 'valid_data'
    '''
    manage_bd.del_table(name)


delete_all_table_t()
# print(manage_bd.path_to("t_bd"))