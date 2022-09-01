-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2022 at 05:37 PM
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
-- Table structure for table `bank_accounts`
--

CREATE TABLE `bank_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL,
  `account_number` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL,
  `security_code` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cash_accounts`
--

CREATE TABLE `cash_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `address` text NOT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `branch_name` text DEFAULT NULL,
  `credit_limit` float DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `expense_accounts`
--

CREATE TABLE `expense_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `income_accounts`
--

CREATE TABLE `income_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `income_account_name` text NOT NULL,
  `total_amount` int(11) NOT NULL,
  `income_account_id` int(11) DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `invoice_id` int(11) DEFAULT NULL,
  `invoice_type` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `exp_account_name` text NOT NULL,
  `total_amount` varchar(255) NOT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `exp_account_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

-- --------------------------------------------------------

--
-- Table structure for table `rx_invoices`
--

CREATE TABLE `rx_invoices` (
  `id` int(11) NOT NULL,
  `issue_date` text NOT NULL,
  `due_date` text NOT NULL,
  `reference` text DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `customer_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text DEFAULT NULL,
  `item_qty` int(11) DEFAULT NULL,
  `sales_price` float DEFAULT NULL,
  `total_amount` float NOT NULL,
  `od_size` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `os_size` text DEFAULT NULL,
  `os_sph` text DEFAULT NULL,
  `os_cyl` text DEFAULT NULL,
  `os_axis` text DEFAULT NULL,
  `os_add` text DEFAULT NULL,
  `os_base` text DEFAULT NULL,
  `os_fh` text DEFAULT NULL,
  `os_prism_detail` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `bvd_mm` text DEFAULT NULL,
  `face_angle` text DEFAULT NULL,
  `pantoscopic_Angle` text DEFAULT NULL,
  `nrd` text DEFAULT NULL,
  `decentration` text DEFAULT NULL,
  `center_edge` text DEFAULT NULL,
  `oc_height` text DEFAULT NULL,
  `occupation` text DEFAULT NULL,
  `driving` text DEFAULT NULL,
  `computer` text DEFAULT NULL,
  `reading` text DEFAULT NULL,
  `mobile` text DEFAULT NULL,
  `gaming` text DEFAULT NULL,
  `od_cost_price` float DEFAULT NULL,
  `od_sales_price` float DEFAULT NULL,
  `od_qty` int(11) DEFAULT NULL,
  `os_cost_price` float DEFAULT NULL,
  `os_sales_price` float DEFAULT NULL,
  `os_qty` int(11) DEFAULT NULL,
  `od_pd` text DEFAULT NULL,
  `os_pd` text DEFAULT NULL,
  `frame_size_h` text DEFAULT NULL,
  `frame_size_v` text DEFAULT NULL,
  `frame_size_d` text DEFAULT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `discount` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `status` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `qty` int(11) DEFAULT NULL,
  `service_cost` float DEFAULT NULL,
  `description` text DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `income_account_id` int(11) NOT NULL,
  `expense_account_id` int(11) NOT NULL,
  `income_account_name` text DEFAULT NULL,
  `expense_account_name` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `description` text DEFAULT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `od_prism_no` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `os_sph` text NOT NULL,
  `os_cyl` text NOT NULL,
  `os_axis` text NOT NULL,
  `os_add` text NOT NULL,
  `os_base` text NOT NULL,
  `os_fh` text NOT NULL,
  `os_prism_no` text DEFAULT NULL,
  `os_prism_detail` text NOT NULL,
  `bvd_mm` text NOT NULL,
  `face_angle` text NOT NULL,
  `pantoscopic_Angle` text NOT NULL,
  `nrd` text NOT NULL,
  `decentration` text NOT NULL,
  `center_edge` text NOT NULL,
  `frame_size_h` text NOT NULL,
  `oc_height` text NOT NULL,
  `od1` text DEFAULT NULL,
  `os1` text DEFAULT NULL,
  `occupation` text NOT NULL,
  `driving` text NOT NULL,
  `computer` text NOT NULL,
  `reading` text NOT NULL,
  `mobile` text NOT NULL,
  `gaming` text NOT NULL,
  `status` text NOT NULL,
  `od_size` text NOT NULL,
  `os_size` text NOT NULL,
  `od_cost_price` float NOT NULL,
  `od_sales_price` float NOT NULL,
  `od_qty` int(11) NOT NULL,
  `os_cost_price` float NOT NULL,
  `os_sales_price` float NOT NULL,
  `os_qty` int(11) NOT NULL,
  `od_pd` text NOT NULL,
  `os_pd` text NOT NULL,
  `total_amount` float NOT NULL,
  `frame_size_v` text NOT NULL,
  `frame_size_d` text NOT NULL,
  `income_account_id` int(11) NOT NULL,
  `expense_account_id` int(11) NOT NULL,
  `income_account_name` text NOT NULL,
  `expense_account_name` text NOT NULL,
  `treatment_id` int(11) DEFAULT NULL,
  `discount` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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

-- --------------------------------------------------------

--
-- Table structure for table `rx_purchases`
--

CREATE TABLE `rx_purchases` (
  `id` int(11) NOT NULL,
  `issue_date` text DEFAULT NULL,
  `due_date` text DEFAULT NULL,
  `reference` text DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `supplier_name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text DEFAULT NULL,
  `item_qty` int(11) DEFAULT NULL,
  `cost_price` float DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  `status` text DEFAULT NULL,
  `od_size` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `os_size` text DEFAULT NULL,
  `os_sph` text DEFAULT NULL,
  `os_cyl` text NOT NULL,
  `os_axis` text NOT NULL,
  `os_add` text NOT NULL,
  `os_base` text NOT NULL,
  `os_fh` text NOT NULL,
  `os_prism_detail` text NOT NULL,
  `bvd_mm` text NOT NULL,
  `face_angle` text NOT NULL,
  `pantoscopic_Angle` text NOT NULL,
  `nrd` text NOT NULL,
  `decentration` text NOT NULL,
  `center_edge` text NOT NULL,
  `oc_height` text NOT NULL,
  `occupation` text NOT NULL,
  `driving` text NOT NULL,
  `computer` text NOT NULL,
  `reading` text NOT NULL,
  `mobile` text NOT NULL,
  `gaming` text NOT NULL,
  `od_cost_price` float NOT NULL,
  `od_sales_price` float NOT NULL,
  `od_qty` text NOT NULL,
  `os_cost_price` float NOT NULL,
  `os_sales_price` float NOT NULL,
  `os_qty` text NOT NULL,
  `od_pd` text NOT NULL,
  `os_pd` text NOT NULL,
  `frame_size_h` text NOT NULL,
  `frame_size_v` text NOT NULL,
  `frame_size_d` text NOT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stock_invoices`
--

CREATE TABLE `stock_invoices` (
  `id` int(11) NOT NULL,
  `issue_date` text NOT NULL,
  `due_date` text NOT NULL,
  `reference` text NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `customer_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text DEFAULT NULL,
  `item_qty` int(11) DEFAULT NULL,
  `sales_price` float DEFAULT NULL,
  `total_amount` float NOT NULL,
  `od_size` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `os_size` text DEFAULT NULL,
  `os_sph` text DEFAULT NULL,
  `os_cyl` text DEFAULT NULL,
  `os_axis` text DEFAULT NULL,
  `os_add` text DEFAULT NULL,
  `os_base` text DEFAULT NULL,
  `os_fh` text DEFAULT NULL,
  `os_prism_detail` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `bvd_mm` text DEFAULT NULL,
  `face_angle` text DEFAULT NULL,
  `pantoscopic_Angle` text DEFAULT NULL,
  `nrd` text DEFAULT NULL,
  `decentration` text DEFAULT NULL,
  `center_edge` text DEFAULT NULL,
  `oc_height` text DEFAULT NULL,
  `occupation` text DEFAULT NULL,
  `driving` text DEFAULT NULL,
  `computer` text DEFAULT NULL,
  `reading` text DEFAULT NULL,
  `mobile` text DEFAULT NULL,
  `gaming` text DEFAULT NULL,
  `od_cost_price` float DEFAULT NULL,
  `od_sales_price` float DEFAULT NULL,
  `od_qty` int(11) DEFAULT NULL,
  `os_cost_price` float DEFAULT NULL,
  `os_sales_price` float DEFAULT NULL,
  `os_qty` int(11) DEFAULT NULL,
  `od_pd` text DEFAULT NULL,
  `os_pd` text DEFAULT NULL,
  `frame_size_h` text DEFAULT NULL,
  `frame_size_v` text DEFAULT NULL,
  `frame_size_d` text DEFAULT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `discount` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `status` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stock_items`
--

CREATE TABLE `stock_items` (
  `id` int(11) NOT NULL,
  `item_code` text DEFAULT NULL,
  `lense_type` text NOT NULL,
  `unit_name` text NOT NULL,
  `purchase_price` float NOT NULL,
  `sales_price` float NOT NULL,
  `qty` int(11) DEFAULT NULL,
  `service_cost` float DEFAULT NULL,
  `description` text DEFAULT NULL,
  `total_cost` float DEFAULT NULL,
  `income_account` int(11) NOT NULL,
  `expense_account` int(11) NOT NULL,
  `last_updated` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stock_orders`
--

CREATE TABLE `stock_orders` (
  `id` int(11) NOT NULL,
  `date` text NOT NULL,
  `reference` text NOT NULL,
  `order_number` text DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text DEFAULT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `od_prism_no` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `os_sph` text NOT NULL,
  `os_cyl` text NOT NULL,
  `os_axis` text NOT NULL,
  `os_add` text NOT NULL,
  `os_base` text DEFAULT NULL,
  `os_fh` text DEFAULT NULL,
  `os_prism_no` text DEFAULT NULL,
  `os_prism_detail` text DEFAULT NULL,
  `bvd_mm` text DEFAULT NULL,
  `face_angle` text DEFAULT NULL,
  `pantoscopic_Angle` text DEFAULT NULL,
  `nrd` text DEFAULT NULL,
  `decentration` text DEFAULT NULL,
  `center_edge` text DEFAULT NULL,
  `frame_size_h` text DEFAULT NULL,
  `oc_height` text DEFAULT NULL,
  `od1` text DEFAULT NULL,
  `os1` text DEFAULT NULL,
  `occupation` text DEFAULT NULL,
  `driving` text DEFAULT NULL,
  `computer` text DEFAULT NULL,
  `reading` text DEFAULT NULL,
  `mobile` text DEFAULT NULL,
  `gaming` text DEFAULT NULL,
  `status` text NOT NULL,
  `od_size` text NOT NULL,
  `os_size` text NOT NULL,
  `od_cost_price` float NOT NULL,
  `od_sales_price` float NOT NULL,
  `od_qty` int(11) NOT NULL,
  `os_cost_price` float NOT NULL,
  `os_sales_price` float NOT NULL,
  `os_qty` int(11) NOT NULL,
  `od_pd` text DEFAULT NULL,
  `os_pd` text DEFAULT NULL,
  `total_amount` float NOT NULL,
  `frame_size_v` text DEFAULT NULL,
  `frame_size_d` text DEFAULT NULL,
  `discount` varchar(255) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `stock_purchases`
--

CREATE TABLE `stock_purchases` (
  `id` int(11) NOT NULL,
  `issue_date` text DEFAULT NULL,
  `due_date` text DEFAULT NULL,
  `reference` text DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `supplier_name` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text DEFAULT NULL,
  `item_qty` int(11) DEFAULT NULL,
  `cost_price` float DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  `status` text DEFAULT NULL,
  `od_size` text DEFAULT NULL,
  `od_sph` text DEFAULT NULL,
  `od_cyl` text DEFAULT NULL,
  `od_axis` text DEFAULT NULL,
  `od_add` text DEFAULT NULL,
  `od_base` text DEFAULT NULL,
  `od_fh` text DEFAULT NULL,
  `od_prism_detail` text DEFAULT NULL,
  `os_size` text DEFAULT NULL,
  `os_sph` text DEFAULT NULL,
  `os_cyl` text NOT NULL,
  `os_axis` text NOT NULL,
  `os_add` text NOT NULL,
  `os_base` text DEFAULT NULL,
  `os_fh` text DEFAULT NULL,
  `os_prism_detail` text DEFAULT NULL,
  `bvd_mm` text DEFAULT NULL,
  `face_angle` text DEFAULT NULL,
  `pantoscopic_Angle` text DEFAULT NULL,
  `nrd` text DEFAULT NULL,
  `decentration` text DEFAULT NULL,
  `center_edge` text DEFAULT NULL,
  `oc_height` text DEFAULT NULL,
  `occupation` text DEFAULT NULL,
  `driving` text DEFAULT NULL,
  `computer` text DEFAULT NULL,
  `reading` text DEFAULT NULL,
  `mobile` text DEFAULT NULL,
  `gaming` text DEFAULT NULL,
  `od_cost_price` float NOT NULL,
  `od_sales_price` float DEFAULT NULL,
  `od_qty` text NOT NULL,
  `os_cost_price` float NOT NULL,
  `os_sales_price` float DEFAULT NULL,
  `os_qty` text NOT NULL,
  `od_pd` text DEFAULT NULL,
  `os_pd` text DEFAULT NULL,
  `frame_size_h` text DEFAULT NULL,
  `frame_size_v` text DEFAULT NULL,
  `frame_size_d` text DEFAULT NULL,
  `treatment` text DEFAULT NULL,
  `tint_service` text DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `description` text NOT NULL,
  `actual_bal` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tints_of_services`
--

CREATE TABLE `tints_of_services` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `treatments`
--

CREATE TABLE `treatments` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `type` varchar(255) NOT NULL,
  `branch_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bank_accounts`
--
ALTER TABLE `bank_accounts`
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
-- Indexes for table `cash_accounts`
--
ALTER TABLE `cash_accounts`
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
-- Indexes for table `expense_accounts`
--
ALTER TABLE `expense_accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `income_accounts`
--
ALTER TABLE `income_accounts`
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
-- Indexes for table `stock_invoices`
--
ALTER TABLE `stock_invoices`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_items`
--
ALTER TABLE `stock_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_orders`
--
ALTER TABLE `stock_orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stock_purchases`
--
ALTER TABLE `stock_purchases`
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
-- AUTO_INCREMENT for table `bank_accounts`
--
ALTER TABLE `bank_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `branch`
--
ALTER TABLE `branch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cash_accounts`
--
ALTER TABLE `cash_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `expense_accounts`
--
ALTER TABLE `expense_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `income_accounts`
--
ALTER TABLE `income_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inoutreceipts`
--
ALTER TABLE `inoutreceipts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `lense_types`
--
ALTER TABLE `lense_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `pricing`
--
ALTER TABLE `pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rx_invoices`
--
ALTER TABLE `rx_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rx_items`
--
ALTER TABLE `rx_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rx_orders`
--
ALTER TABLE `rx_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rx_orders_old`
--
ALTER TABLE `rx_orders_old`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rx_purchases`
--
ALTER TABLE `rx_purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock_invoices`
--
ALTER TABLE `stock_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock_items`
--
ALTER TABLE `stock_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock_orders`
--
ALTER TABLE `stock_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stock_purchases`
--
ALTER TABLE `stock_purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tints_of_services`
--
ALTER TABLE `tints_of_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `treatments`
--
ALTER TABLE `treatments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
