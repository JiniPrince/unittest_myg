# test_dropdown.py

from FlexContainer_dropdown.dropdown.dropdown import DropdownList

def test_get_dropdown_items():
    dropdown_list = DropdownList()

    assert dropdown_list.get_dropdown_items('E-MI Claims') == ['Item 1', 'Item 2', 'Item 3']
    assert dropdown_list.get_dropdown_items('New Arrivals') == ['Item 4', 'Item 5', 'Item 6']
    assert dropdown_list.get_dropdown_items('Home Appliances') == ['Item 7', 'Item 8', 'Item 9']
    assert dropdown_list.get_dropdown_items('Mobiles') == ['Item 10', 'Item 11', 'Item 12']
    assert dropdown_list.get_dropdown_items('Laptops') == ['Item 13', 'Item 14', 'Item 15']

def test_add_dropdown_item():
    dropdown_list = DropdownList()

    dropdown_list.add_dropdown_item('New Item 1', 'E-MI Claims')
    assert 'New Item 1' in dropdown_list.get_dropdown_items('E-MI Claims')

    dropdown_list.add_dropdown_item('New Item 2', 'New Arrivals')
    assert 'New Item 2' in dropdown_list.get_dropdown_items('New Arrivals')

    dropdown_list.add_dropdown_item('New Item 3', 'Home Appliances')
    assert 'New Item 3' in dropdown_list.get_dropdown_items('Home Appliances')

    dropdown_list.add_dropdown_item('New Item 4', 'Mobiles')
    assert 'New Item 4' in dropdown_list.get_dropdown_items('Mobiles')

    dropdown_list.add_dropdown_item('New Item 5', 'Laptops')
    assert 'New Item 5' in dropdown_list.get_dropdown_items('Laptops')




def test_remove_dropdown_item():
    dropdown_list = DropdownList()

    dropdown_list.remove_dropdown_item('Item 1', 'E-MI Claims')
    assert 'Item 1' not in dropdown_list.get_dropdown_items('E-MI Claims')

    dropdown_list.remove_dropdown_item('Item 4', 'New Arrivals')
    assert 'Item 4' not in dropdown_list.get_dropdown_items('New Arrivals')

    dropdown_list.remove_dropdown_item('Item 7', 'Home Appliances')
    assert 'Item 7' not in dropdown_list.get_dropdown_items('Home Appliances')

    dropdown_list.remove_dropdown_item('Item 11', 'Mobiles')
    assert 'Item 11' not in dropdown_list.get_dropdown_items('Mobiles')
