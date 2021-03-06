-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2022 at 06:47 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lenses`
--

-- --------------------------------------------------------

--
-- Table structure for table `bankandcashaccounts`
--

CREATE TABLE `bankandcashaccounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bankandcashaccounts`
--

INSERT INTO `bankandcashaccounts` (`id`, `name`, `code`, `actual_balance`) VALUES
(1, 'Cash in Hand', 'CIH', 200),
(3, 'account1', '1', 0),
(4, 'account2', '2', 400),
(5, 'testing', 'TEST', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL,
  `security_code` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`id`, `name`, `phone`, `address`, `security_code`) VALUES
(1, 'my branch', '213123123', 'RR-132 PEHCS', 'abc');

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`id`, `name`, `description`) VALUES
(1, 'groot brand', 'this is desc'),
(3, 'asiasd', 'asdasd');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `description`) VALUES
(3, 'new category', 'this is description');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `email`, `phone`, `address`) VALUES
(2, 'abc', 'asdsa@adsdas.com', '65465456465', 'asdsadsad'),
(3, 'Groot', 'groot@test.com', '03232323232', 'R-1231293 PECHS');

-- --------------------------------------------------------

--
-- Table structure for table `inoutreceipts`
--

CREATE TABLE `inoutreceipts` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `reference` text DEFAULT NULL,
  `paid_by_account_type` text NOT NULL,
  `paid_by_account_id` int(11) DEFAULT NULL,
  `paid_by_account_name` text NOT NULL,
  `received_in_account_id` int(11) NOT NULL,
  `received_in_account_name` text DEFAULT NULL,
  `description` text NOT NULL,
  `exp_account` text NOT NULL,
  `total_amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inoutreceipts`
--

INSERT INTO `inoutreceipts` (`id`, `date`, `reference`, `paid_by_account_type`, `paid_by_account_id`, `paid_by_account_name`, `received_in_account_id`, `received_in_account_name`, `description`, `exp_account`, `total_amount`) VALUES
(4, '2022-07-01', 'sdad', 'supplier', 1, 'sup 1 ', 1, 'Cash in Hand', 'asdasd', 'Accounting feesExpenses', 450000),
(5, '2022-07-07', 'no ref', 'customer', 1, 'Groot', 1, 'Cash in Hand', 'this is desc', 'Printing and stationery', 200),
(6, '2022-07-29', 'ref', 'customer', 3, 'Groot', 4, 'account2', 'received rent from groot customer', 'Accounting feesExpenses', 200);

-- --------------------------------------------------------

--
-- Table structure for table `lense_types`
--

CREATE TABLE `lense_types` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `lense_category_id` int(11) NOT NULL,
  `lense_brand_id` int(11) NOT NULL,
  `left_right_pair` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lense_types`
--

INSERT INTO `lense_types` (`id`, `name`, `description`, `lense_category_id`, `lense_brand_id`, `left_right_pair`) VALUES
(1, 'my z lense', 'this is desc', 3, 1, 0),
(2, 'this is y lense', 'desc', 3, 1, 0),
(3, 'asdasjd', 'asdkjaskdj', 3, 1, 0),
(4, 'asdasd', 'dsadasd', 3, 1, 1),
(6, 'pqwepqwe', 'asdasdas', 3, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `reference` text DEFAULT NULL,
  `paid_from_account_id` int(11) NOT NULL,
  `paid_from_account_name` text NOT NULL,
  `payee_type` text NOT NULL,
  `payee_id` int(11) DEFAULT NULL,
  `payee_name` text NOT NULL,
  `description` text DEFAULT NULL,
  `exp_account` text NOT NULL,
  `total_amount` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `date`, `reference`, `paid_from_account_id`, `paid_from_account_name`, `payee_type`, `payee_id`, `payee_name`, `description`, `exp_account`, `total_amount`) VALUES
(2, '2022-07-01', 'ref', 1, 'Cash in Hand', 'customer', 1, '', 'this is desc', 'Legal fees', '100'),
(3, '2022-07-29', 'ref', 5, '3', 'customer', 3, '', 'pay rent to groot customer', 'Rent', '200');

-- --------------------------------------------------------

--
-- Table structure for table `pricing`
--

CREATE TABLE `pricing` (
  `id` int(11) NOT NULL,
  `lense_name` text NOT NULL,
  `cylinder` varchar(255) NOT NULL,
  `spherical` varchar(255) NOT NULL,
  `quantity_left` int(11) NOT NULL,
  `quantity_right` int(11) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pricing`
--

INSERT INTO `pricing` (`id`, `lense_name`, `cylinder`, `spherical`, `quantity_left`, `quantity_right`, `price`) VALUES
(1, 'my z lense', '0.25', '0.25', 10, 20, 2000);

-- --------------------------------------------------------

--
-- Table structure for table `rx_invoices`
--

CREATE TABLE `rx_invoices` (
  `id` int(11) NOT NULL,
  `issue_date` text NOT NULL,
  `due_date` text NOT NULL,
  `reference` text NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text NOT NULL,
  `item_qty` int(11) NOT NULL,
  `item_price` float NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_invoices`
--

INSERT INTO `rx_invoices` (`id`, `issue_date`, `due_date`, `reference`, `customer_id`, `customer_name`, `billing_address`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `item_price`, `total`) VALUES
(4, '2022-07-29', '2022-07-09', 'ref', 3, 'Groot', 'R-1231293 PECHS', 'sold 2 optolux for 300', 4, 'developer lense', 'Accounting feesExpenses', 1, 150, 150),
(5, '2022-07-29', '2022-06-30', 'order3', 2, 'abc', 'asdsadsad', 'desc', 1, 'OPTOLUX 3.0 UHD 1.67 LITE++ BLUE FIGHTER CLARION', 'Accounting feesExpenses', 20, 2, 40);

-- --------------------------------------------------------

--
-- Table structure for table `rx_items`
--

CREATE TABLE `rx_items` (
  `id` int(11) NOT NULL,
  `item_code` text DEFAULT NULL,
  `lense_type` text NOT NULL,
  `unit_name` text NOT NULL,
  `purchase_price` float NOT NULL,
  `sales_price` float NOT NULL,
  `qty` int(11) NOT NULL,
  `service_cost` float NOT NULL,
  `description` text DEFAULT NULL,
  `total_cost` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_items`
--

INSERT INTO `rx_items` (`id`, `item_code`, `lense_type`, `unit_name`, `purchase_price`, `sales_price`, `qty`, `service_cost`, `description`, `total_cost`) VALUES
(1, '3.0 1.67 BF', 'OPTOLUX 3.0 UHD 1.67 LITE++ BLUE FIGHTER CLARION', 'Piece', 11, 12, 40, 13, 'dec', 14),
(4, 'Gr', 'developer lense', 'unit name', 2000, 3000, 9, 50, NULL, 2050);

-- --------------------------------------------------------

--
-- Table structure for table `rx_orders`
--

CREATE TABLE `rx_orders` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `reference` text NOT NULL,
  `order_number` text DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text NOT NULL,
  `treatment` text NOT NULL,
  `tint_service` text NOT NULL,
  `od_sph` text NOT NULL,
  `od_cyl` text NOT NULL,
  `od_axis` text NOT NULL,
  `od_add` text NOT NULL,
  `od_base` text NOT NULL,
  `od_fh` text NOT NULL,
  `od_prism_no` text NOT NULL,
  `od_prism_detail` text NOT NULL,
  `os_sph` text NOT NULL,
  `os_cyl` text NOT NULL,
  `os_axis` text NOT NULL,
  `os_add` text NOT NULL,
  `os_base` text NOT NULL,
  `os_fh` text NOT NULL,
  `os_prism_no` text NOT NULL,
  `os_prism_detail` text NOT NULL,
  `bvd_mm` text NOT NULL,
  `face_angle` text NOT NULL,
  `pantoscopic_Angle` text NOT NULL,
  `nrd` text NOT NULL,
  `decentration` text NOT NULL,
  `center_edge` text NOT NULL,
  `frame_size_h` text NOT NULL,
  `oc_height` text NOT NULL,
  `od1` text NOT NULL,
  `os1` text NOT NULL,
  `occupation` text NOT NULL,
  `driving` text NOT NULL,
  `computer` text NOT NULL,
  `reading` text NOT NULL,
  `mobile` text NOT NULL,
  `gaming` text NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_orders`
--

INSERT INTO `rx_orders` (`id`, `date`, `reference`, `order_number`, `customer_id`, `customer_name`, `item_id`, `item_name`, `billing_address`, `description`, `treatment`, `tint_service`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `od_prism_no`, `od_prism_detail`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_no`, `os_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `frame_size_h`, `oc_height`, `od1`, `os1`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `status`) VALUES
(8, '2022-07-23', '2ref2', 'order3', 1, 'Groot', 1, 'OPTOLUX 3.0 UHD 1.67 LITE++ BLUE FIGHTER CLARION', 'R-1231293 PECHS', 'desc', 'treat', 'tints', '1', '1', '1', '1', '1', '10', '1t', '1t', '1', '1', '1', '1', '1', '10', '1t', '1t', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', 'ready');

-- --------------------------------------------------------

--
-- Table structure for table `rx_orders_old`
--

CREATE TABLE `rx_orders_old` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `reference` text DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `item_desc` text NOT NULL,
  `item_qty` int(11) NOT NULL,
  `item_price` float NOT NULL,
  `total` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_orders_old`
--

INSERT INTO `rx_orders_old` (`id`, `date`, `reference`, `customer_id`, `customer_name`, `billing_address`, `description`, `item_id`, `item_name`, `item_desc`, `item_qty`, `item_price`, `total`) VALUES
(2, '2022-07-06', 'ref', 1, 'Groot', 'R12211`', 'desc', 0, 'item xyz', 'idees', 2, 100, 200);

-- --------------------------------------------------------

--
-- Table structure for table `rx_purchases`
--

CREATE TABLE `rx_purchases` (
  `id` int(11) NOT NULL,
  `issue_date` text NOT NULL,
  `due_date` text NOT NULL,
  `reference` text NOT NULL,
  `supplier_id` int(11) NOT NULL,
  `supplier_name` text NOT NULL,
  `description` text NOT NULL,
  `item_id` int(11) DEFAULT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text NOT NULL,
  `item_qty` int(11) NOT NULL,
  `item_price` float NOT NULL,
  `total` float NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_purchases`
--

INSERT INTO `rx_purchases` (`id`, `issue_date`, `due_date`, `reference`, `supplier_id`, `supplier_name`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `item_price`, `total`, `status`) VALUES
(2, '2022-07-29', '2022-07-02', 'ref', 1, 'sup 1 ', 'purchased 10 opt for 40000', 4, 'developer lense', 'Accounting feesExpenses', 10, 4000, 32000, 'pending'),
(4, '2022-07-29', '2022-06-29', 'order3', 1, 'sup 1', 'desc', 1, 'OPTOLUX 3.0 UHD 1.67 LITE++ BLUE FIGHTER CLARION', 'Accounting feesExpenses', 50, 100, 5000, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`id`, `name`, `email`, `phone`, `address`, `description`) VALUES
(1, 'sup 1', 'sup1@gmail.com', '23093029', 'R-1332ad', 'descr'),
(3, 'sup 1 2', 'sup1@gmail.com', '23093029', 'R-1332ad', 'descr');

-- --------------------------------------------------------

--
-- Table structure for table `tints_of_services`
--

CREATE TABLE `tints_of_services` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tints_of_services`
--

INSERT INTO `tints_of_services` (`id`, `name`, `description`) VALUES
(5, 'service b', 'desc');

-- --------------------------------------------------------

--
-- Table structure for table `treatments`
--

CREATE TABLE `treatments` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `treatments`
--

INSERT INTO `treatments` (`id`, `name`, `description`) VALUES
(1, 'treatment no12', 'desc');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` text NOT NULL,
  `branch` text NOT NULL,
  `password` varchar(255) NOT NULL,
  `security_code` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `branch`, `password`, `security_code`, `type`) VALUES
(3, 'groot', 'groot@dev.com', 'my branch', '123', 'ABC', 'user'),
(4, 'admin', 'admin@admin.com', 'my branch', 'admin', 'admin', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bankandcashaccounts`
--
ALTER TABLE `bankandcashaccounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inoutreceipts`
--
ALTER TABLE `inoutreceipts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lense_types`
--
ALTER TABLE `lense_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pricing`
--
ALTER TABLE `pricing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rx_invoices`
--
ALTER TABLE `rx_invoices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rx_items`
--
ALTER TABLE `rx_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rx_orders`
--
ALTER TABLE `rx_orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rx_orders_old`
--
ALTER TABLE `rx_orders_old`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rx_purchases`
--
ALTER TABLE `rx_purchases`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tints_of_services`
--
ALTER TABLE `tints_of_services`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `treatments`
--
ALTER TABLE `treatments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bankandcashaccounts`
--
ALTER TABLE `bankandcashaccounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `branch`
--
ALTER TABLE `branch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `inoutreceipts`
--
ALTER TABLE `inoutreceipts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `lense_types`
--
ALTER TABLE `lense_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pricing`
--
ALTER TABLE `pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `rx_invoices`
--
ALTER TABLE `rx_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `rx_items`
--
ALTER TABLE `rx_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `rx_orders`
--
ALTER TABLE `rx_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `rx_orders_old`
--
ALTER TABLE `rx_orders_old`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rx_purchases`
--
ALTER TABLE `rx_purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tints_of_services`
--
ALTER TABLE `tints_of_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `treatments`
--
ALTER TABLE `treatments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
