INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Latte', 'Our dark, rich espresso balanced with steamed milk and a light layer of foam. ', 5.00, 100, 'static/images/latte.jpeg', 'Coffee');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Cappuccino', 'Dark, rich espresso lies in wait under a smoothed and stretched layer of thick milk foam.', 5.00, 100, 'static/images/c.jpeg', 'Coffee');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Macchiato', 'Our rich espresso marked with dollop of steamed milk and foam.', 5.00, 100, 'static/images/macc.jpeg', 'Coffee');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES('Caramel Latte', 'Rich espresso with caramel flavor', 4.99, 10, 'static/images/caramel.jpeg', 'Coffee');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Espresso Shot', 'Strong and concentrated coffee.', 5.00, 100, 'static/images/espresso.jpeg', 'Coffee');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`,`espresso_count`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 10, 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`,`espresso_count`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 10, 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`,`espresso_count`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 10, 5.50);
