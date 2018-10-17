#to-do: add ui

#test run through
w1(w@gmail.com, 1111)
w2(w@yahoo.com, 0000)

w1.checkBalance(1111)
w2.checkBalance(0000)

w1.addFunds(50, acct, 1111)
w1.checkBalance(1111)

w1.payment(20, w2)

w1.checkBalance(1111)
w2.checkBalance(0000)
