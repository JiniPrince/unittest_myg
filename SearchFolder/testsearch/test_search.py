from SearchFolder.search.search import Product_search,Myg_store
def test_search_products():
    store = Myg_store()

    # Add some products to the store
    store.add_product(Product_search("Samsung TV", "TV", 499.99))
    store.add_product(Product_search("LG Refrigerator", "Home Appliance", 899.99))
    store.add_product(Product_search("Apple iPhone", "Mobile", 699.99))
    store.add_product(Product_search("Dell Laptop", "Laptop", 999.99))

    # Search for products by keyword
    assert len(store.search_products(keyword="Samsung")) == 1
    assert len(store.search_products(keyword="Apple")) == 1
    assert len(store.search_products(keyword="Dell")) == 1

    # Search for products by category
    assert len(store.search_products(category="TV")) == 1
    assert len(store.search_products(category="Mobile")) == 1
    assert len(store.search_products(category="Laptop")) == 1

    # Search for products that don't exist
    assert len(store.search_products(keyword="Xbox")) == 0
    assert len(store.search_products(category="Washing Machine")) == 0
