-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2022 at 03:26 AM
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
  `actual_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bank_accounts`
--

INSERT INTO `bank_accounts` (`id`, `name`, `code`, `actual_balance`) VALUES
(3, 'account1', '1', 0),
(4, 'account2', '2', 400),
(5, 'testing', 'TEST', 1000),
(6, 'Meezan Bank', 'MB', 9000);

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
-- Table structure for table `cash_accounts`
--

CREATE TABLE `cash_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cash_accounts`
--

INSERT INTO `cash_accounts` (`id`, `name`, `code`, `actual_balance`) VALUES
(1, 'Cash In Hand', 'CIH', 5000);

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
-- Table structure for table `expense_accounts`
--

CREATE TABLE `expense_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense_accounts`
--

INSERT INTO `expense_accounts` (`id`, `name`, `code`, `actual_balance`) VALUES
(4, 'account2', '2', 400),
(5, 'testing', 'TEST', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `income_accounts`
--

CREATE TABLE `income_accounts` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `code` varchar(255) DEFAULT NULL,
  `actual_balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `income_accounts`
--

INSERT INTO `income_accounts` (`id`, `name`, `code`, `actual_balance`) VALUES
(3, 'account1', '1', 0),
(4, 'account2', '2', 400),
(5, 'testing', 'TEST', 1000);

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
  `description` text DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text NOT NULL,
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
  `tint_service` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_invoices`
--

INSERT INTO `rx_invoices` (`id`, `issue_date`, `due_date`, `reference`, `customer_id`, `customer_name`, `billing_address`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `sales_price`, `total_amount`, `od_size`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `os_size`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_detail`, `od_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `oc_height`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `od_cost_price`, `od_sales_price`, `od_qty`, `os_cost_price`, `os_sales_price`, `os_qty`, `od_pd`, `os_pd`, `frame_size_h`, `frame_size_v`, `frame_size_d`, `treatment`, `tint_service`) VALUES
(10, '2022-08-01', '2022-08-01', '10', 0, ' abc', ' asdsadsad', NULL, 5, ' grootex lens', 'Accounting feesExpenses', NULL, NULL, 2340, ' od_size', ' 1', ' 2', ' 3', ' 4', ' 5', ' 10', ' os_size', ' 8', ' 7', ' 6', ' 5', ' 4', ' 10', ' 2', ' 7', ' bvd', ' ffa', ' pa', ' nrd', ' dec', ' ct', ' och', ' occ', ' dr', ' com', ' read', ' mob', ' gam', NULL, 30, 40, NULL, 30, 38, ' 8', ' 1', ' fsh', ' fsv', ' fsd', ' treatment no12', ' service b'),
(15, '2022-08-13', '2022-08-11', '19', 0, ' abc', ' asdsadsad', NULL, 5, ' grootex lens', 'Capital gains on investments', NULL, NULL, 2340, ' od_size', ' 1', ' 2', ' 3', ' 4', ' 5', ' 10', ' os_size', ' 8', ' 7', ' 6', ' 5', ' 4', ' 10', ' 2', ' 7', ' bvd', ' ffa', ' pa', ' nrd', ' dec', ' ct', ' och', ' occ', ' dr', ' com', ' read', ' mob', ' gam', NULL, 30, 40, NULL, 30, 38, ' 8', ' 1', ' fsh', ' fsv', ' fsd', ' treatment no12', ' service b');

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
  `income_account` int(11) NOT NULL,
  `expense_account` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_items`
--

INSERT INTO `rx_items` (`id`, `item_code`, `lense_type`, `unit_name`, `purchase_price`, `sales_price`, `qty`, `service_cost`, `description`, `total_cost`, `income_account`, `expense_account`) VALUES
(1, '3.0 1.67 BF', 'OPTOLUX 3.0 UHD 1.67 LITE++ BLUE FIGHTER CLARION', 'Piece', 11, 12, 40, 13, 'dec', 14, 5, 4),
(4, 'Gr', 'developer lense', 'unit name', 2000, 3000, 9, 50, NULL, 2050, 5, 4),
(5, 'item code', 'grootex lens', 'unit name', 20, 30, NULL, NULL, NULL, NULL, 5, 4),
(6, '0202', 'example', 'exam', 2, 2, NULL, NULL, NULL, NULL, 5, 4),
(7, 'L2', 'L2', 'L2', 3, 4, NULL, NULL, NULL, NULL, 4, 5);

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
  `expense_account_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_orders`
--

INSERT INTO `rx_orders` (`id`, `date`, `reference`, `order_number`, `customer_id`, `customer_name`, `item_id`, `item_name`, `billing_address`, `description`, `treatment`, `tint_service`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `od_prism_no`, `od_prism_detail`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_no`, `os_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `frame_size_h`, `oc_height`, `od1`, `os1`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `status`, `od_size`, `os_size`, `od_cost_price`, `od_sales_price`, `od_qty`, `os_cost_price`, `os_sales_price`, `os_qty`, `od_pd`, `os_pd`, `total_amount`, `frame_size_v`, `frame_size_d`, `income_account_id`, `expense_account_id`, `income_account_name`, `expense_account_name`) VALUES
(16, '2022-07-16', 'Noref', 'gos-16', 3, 'Groot', 5, 'grootex lens', 'R-1231293 PECHS', NULL, 'treatment no12', 'service b', '0.25', '0.25', '1', '0.25', '1', '10', NULL, 'de', '0.25', '0.25', '1', '0.25', '1', '10', NULL, 'de', '12', '12', '12', '12', '12', '12', '12', '12', NULL, NULL, '12', '12', '12', '12', '12', '12', 'pending', 'tex2', 'tex2', 20, 30, 2, 0, 0, 0, '', '', 0, '0', '0', 0, 0, '', ''),
(17, '2022-08-04', 'Noref', 'gos-15', 3, 'Groot', 5, 'grootex lens', 'R-1231293 PECHS', NULL, 'treatment no12', 'service b', '0.25', '0.25', '1', '0.25', '1', '10', NULL, 'de', '0.25', '0.25', '1', '0.25', '1', '10', NULL, 'de', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', '12', 'pending', 'tex', 'tex', 20, 30, 2, 0, 0, 0, '', '', 0, '0', '0', 0, 0, '', ''),
(18, '2022-08-12', 'myyref', 'gos-18', 3, 'Groot', 5, 'grootex lens', 'R-1231293 PECHS', NULL, 'treatment no12', 'service b', '-0.25', '0.25', '1', '0.25', '2', '14', NULL, 'r', '-0.25', '0.25', '1', '0.25', '2', '12', NULL, 'r', 'bc', 'ffa', 'dad', 'as', 's', 's', 'a', 'a', NULL, NULL, 'a', 'as', 's', 'c', 'c', 'g', 'pending', 'sz', 'sz', 20, 30, 2, 20, 30, 3, 'dd', 'dd', 0, '0', '0', 0, 0, '', ''),
(19, '2022-08-12', 'REF', 'gos-19', 2, 'abc', 5, 'grootex lens', 'asdsadsad', NULL, 'treatment no12', 'service b', '1', '2', '3', '4', '5', '10', NULL, '7', '8', '7', '6', '5', '4', '10', NULL, '2', 'bvd', 'ffa', 'pa', 'nrd', 'dec', 'ct', 'fsh', 'och', NULL, NULL, 'occ', 'dr', 'com', 'read', 'mob', 'gam', 'ready', 'od_size', 'os_size', 20, 30, 40, 20, 30, 38, '8', '1', 1560, 'fsv', 'fsd', 5, 4, '', ''),
(20, '2022-08-20', 'ref', 'gos-20', 3, 'Groot', 7, 'L2', 'R-1231293 PECHS', NULL, 'treatment no12', 'service b', '', '', '', '', '', '', NULL, '', '', '', '', '', '', '', NULL, '', '', '', '', '', '', '', '', '', NULL, NULL, '', '', '', '', '', '', 'pending', '', '', 3, 4, 2, 3, 4, 2, '', '', 12, '', '', 4, 5, 'account2', 'testing');

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
  `tint_service` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rx_purchases`
--

INSERT INTO `rx_purchases` (`id`, `issue_date`, `due_date`, `reference`, `supplier_id`, `supplier_name`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `cost_price`, `total_amount`, `status`, `od_size`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `od_prism_detail`, `os_size`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `oc_height`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `od_cost_price`, `od_sales_price`, `od_qty`, `os_cost_price`, `os_sales_price`, `os_qty`, `od_pd`, `os_pd`, `frame_size_h`, `frame_size_v`, `frame_size_d`, `treatment`, `tint_service`) VALUES
(22, '2022-08-13', '2022-08-04', '19', 1, 'sup 1', NULL, NULL, ' grootex lens', 'GOS SHAFAY SOFTWARE', NULL, NULL, 1500, NULL, ' od_size', ' 1', ' 2', ' 3', ' 4', ' 5', ' 10', ' 7', ' os_size', ' 8', ' 7', ' 6', ' 5', ' 4', ' 10', ' 2', ' bvd', ' ffa', ' pa', ' nrd', ' dec', ' ct', ' och', ' occ', ' dr', ' com', ' read', ' mob', ' gam', 20, 30, ' 40', 20, 30, ' 38', ' 8', ' 1', ' fsh', ' fsv', ' fsd', ' treatment no12', ' service b'),
(23, '2022-08-13', '2022-08-12', '18', 1, 'sup 1', NULL, NULL, ' grootex lens', 'Advertising and promotion', NULL, NULL, 200, NULL, ' sz', ' -0.25', ' 0.25', ' 1', ' 0.25', ' 2', ' 14', ' r', ' sz', ' -0.25', ' 0.25', ' 1', ' 0.25', ' 2', ' 12', ' r', ' bc', ' ffa', ' dad', ' as', ' s', ' s', ' a', ' a', ' as', ' s', ' c', ' c', ' g', 20, 30, '4', 20, 30, '4', ' dd', ' dd', ' a', ' 0', ' 0', ' treatment no12', ' service b');

-- --------------------------------------------------------

--
-- Table structure for table `stock_invoices`
--

CREATE TABLE `stock_invoices` (
  `id` int(11) NOT NULL,
  `issue_date` text NOT NULL,
  `due_date` text NOT NULL,
  `reference` text NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` text NOT NULL,
  `billing_address` text NOT NULL,
  `description` text DEFAULT NULL,
  `item_id` int(11) NOT NULL,
  `item_name` text DEFAULT NULL,
  `exp_account` text NOT NULL,
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
  `tint_service` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock_invoices`
--

INSERT INTO `stock_invoices` (`id`, `issue_date`, `due_date`, `reference`, `customer_id`, `customer_name`, `billing_address`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `sales_price`, `total_amount`, `od_size`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `os_size`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_detail`, `od_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `oc_height`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `od_cost_price`, `od_sales_price`, `od_qty`, `os_cost_price`, `os_sales_price`, `os_qty`, `od_pd`, `os_pd`, `frame_size_h`, `frame_size_v`, `frame_size_d`, `treatment`, `tint_service`) VALUES
(15, '2022-08-13', '2022-08-11', '19', 0, ' abc', ' asdsadsad', NULL, 5, ' grootex lens', 'Capital gains on investments', NULL, NULL, 2340, ' od_size', ' 1', ' 2', ' 3', ' 4', ' 5', ' 10', ' os_size', ' 8', ' 7', ' 6', ' 5', ' 4', ' 10', ' 2', ' 7', ' bvd', ' ffa', ' pa', ' nrd', ' dec', ' ct', ' och', ' occ', ' dr', ' com', ' read', ' mob', ' gam', NULL, 30, 40, NULL, 30, 38, ' 8', ' 1', ' fsh', ' fsv', ' fsd', ' treatment no12', ' service b');

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
  `frame_size_d` text NOT NULL
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
  `tint_service` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stock_purchases`
--

INSERT INTO `stock_purchases` (`id`, `issue_date`, `due_date`, `reference`, `supplier_id`, `supplier_name`, `description`, `item_id`, `item_name`, `exp_account`, `item_qty`, `cost_price`, `total_amount`, `status`, `od_size`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `od_prism_detail`, `os_size`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `oc_height`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`, `od_cost_price`, `od_sales_price`, `od_qty`, `os_cost_price`, `os_sales_price`, `os_qty`, `od_pd`, `os_pd`, `frame_size_h`, `frame_size_v`, `frame_size_d`, `treatment`, `tint_service`) VALUES
(23, '2022-08-13', '2022-08-12', '18', 1, 'sup 1', NULL, NULL, ' grootex lens', 'Advertising and promotion', NULL, NULL, 200, NULL, ' sz', ' -0.25', ' 0.25', ' 1', ' 0.25', ' 2', ' 14', ' r', ' sz', ' -0.25', ' 0.25', ' 1', ' 0.25', ' 2', ' 12', ' r', ' bc', ' ffa', ' dad', ' as', ' s', ' s', ' a', ' a', ' as', ' s', ' c', ' c', ' g', 20, 30, '4', 20, 30, '4', ' dd', ' dd', ' a', ' 0', ' 0', ' treatment no12', ' service b');

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

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`id`, `name`, `email`, `phone`, `address`, `description`, `actual_bal`) VALUES
(1, 'sup 1', 'sup1@gmail.com', '23093029', 'R-1332ad', 'descr', 1700),
(3, 'sup 2', 'sup1@gmail.com', '23093029', 'R-1332ad', 'descr', 0);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
-- AUTO_INCREMENT for table `cash_accounts`
--
ALTER TABLE `cash_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
-- AUTO_INCREMENT for table `expense_accounts`
--
ALTER TABLE `expense_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `income_accounts`
--
ALTER TABLE `income_accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `rx_items`
--
ALTER TABLE `rx_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `rx_orders`
--
ALTER TABLE `rx_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `rx_orders_old`
--
ALTER TABLE `rx_orders_old`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rx_purchases`
--
ALTER TABLE `rx_purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `stock_invoices`
--
ALTER TABLE `stock_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `stock_orders`
--
ALTER TABLE `stock_orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `stock_purchases`
--
ALTER TABLE `stock_purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
