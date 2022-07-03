-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2022 at 01:00 AM
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
(1, 'Cash in Hand', 'CIH', 200);

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
  `address` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `email`, `phone`, `address`, `description`) VALUES
(1, 'Groot', 'groot@test.com', '03232323232', 'R-1231293 PECHS', 'asdasd desc');

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
(4, '2022-07-01', 'sdad', 'supplier', 1, 'sup 1 ', 1, 'Cash in Hand', 'asdasd', 'Motor vehicle expenses', 450000),
(5, '2022-07-07', 'no ref', 'customer', 1, 'Groot', 1, 'Cash in Hand', 'this is desc', 'Printing and stationery', 200);

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
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer` varchar(255) NOT NULL,
  `lense_type` varchar(255) NOT NULL,
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
  `gaming` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customer`, `lense_type`, `treatment`, `tint_service`, `od_sph`, `od_cyl`, `od_axis`, `od_add`, `od_base`, `od_fh`, `od_prism_no`, `od_prism_detail`, `os_sph`, `os_cyl`, `os_axis`, `os_add`, `os_base`, `os_fh`, `os_prism_no`, `os_prism_detail`, `bvd_mm`, `face_angle`, `pantoscopic_Angle`, `nrd`, `decentration`, `center_edge`, `frame_size_h`, `oc_height`, `od1`, `os1`, `occupation`, `driving`, `computer`, `reading`, `mobile`, `gaming`) VALUES
(3, 'Groot', 'my z lense', 'treat', 'serv', '1', '1', '1', '1', '1', '1', '1', '', '1', '1', '1', '1', '1', '1', '1', '', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '12');

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
(2, '2022-07-01', 'no ref', 1, 'Cash in Hand', 'customer', 1, 'Groot', 'this is desc', 'Legal fees', '100');

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
(1, 'sup 1 ', 'sup1@gmail.com', '23093029', 'R-1332ad', 'descr');

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
-- Indexes for table `orders`
--
ALTER TABLE `orders`
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
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `inoutreceipts`
--
ALTER TABLE `inoutreceipts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `lense_types`
--
ALTER TABLE `lense_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pricing`
--
ALTER TABLE `pricing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
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
