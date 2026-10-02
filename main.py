from pyscript import display, document

order1 = 125 #givng items a value 
order2 = 100
order3 = 200
order4 = 150

def Total_Cost(e): #Getting the total cost of the items
  
    document.getElementById('price').innerHTML = ""
    
    total_sum = 0
    
    
    if document.getElementById('order1').checked:
        total_sum += order1
        
    if document.getElementById('order2').checked:
        total_sum += order2
        
    if document.getElementById('order3').checked:
        total_sum += order3
        
    if document.getElementById('order4').checked:
        total_sum += order4
    display(f'Receipt', target="price")
    display(f'Before VAT 12%: P{total_sum}', target="price") #Total before VAT
    display(f'VAT 12%: P{total_sum*.12}', target="price") #VAT =12%
    display(f'Total: P{total_sum*1.12}', target="price") #This is the total of with the VAT included

    
