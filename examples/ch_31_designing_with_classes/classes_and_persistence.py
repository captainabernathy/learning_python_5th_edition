from pizzashop import PizzaShop
import pickle

if __name__ == '__main__':
    print('code snippets from pages 971-972\n')

    shop = PizzaShop()  # build a PizzaShop
    print(shop.server, shop.chef)  # display shops server and chef
    print('')

    # save shop state
    pickle.dump(shop, open('shopfile.pkl', 'wb'))

    # restore shop
    obj = pickle.load(open('shopfile.pkl', 'rb'))

    print(obj.server, obj.chef)  # output sever and chef
    print('')

    obj.order('LSP')  # process an order

