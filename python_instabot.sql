-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 12, 2021 at 07:49 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_instabot`
--

-- --------------------------------------------------------

--
-- Table structure for table `activites`
--

CREATE TABLE `activites` (
  `id` int(11) NOT NULL,
  `activity_name` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `activites`
--

INSERT INTO `activites` (`id`, `activity_name`) VALUES
(1, 'لایک'),
(2, 'کامنت'),
(3, 'فالو'),
(4, 'دیدن استوری');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `comment_cat` int(11) NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `comment_cat`, `comment`) VALUES
(1, 1, 'محتوا بسیار عالی و جذاب'),
(2, 1, 'مثل همیشه عالی'),
(3, 1, 'خیلی باحال'),
(4, 1, 'قشنگ مشخصه که برای تولید این محتوا ها وقت میگذاری، ممنون از این همه احترامی که برای مخاطبت قائل هستی'),
(5, 1, 'محتواهای بسیار ارزشمندی دارید. '),
(6, 1, 'بسیار عالی ممنون میشم سری هم به صفحه من بزنید'),
(7, 1, 'لایک'),
(8, 1, 'قشنگ بود'),
(9, 1, 'دوست داشتم'),
(10, 1, 'فوق العاده');

-- --------------------------------------------------------

--
-- Table structure for table `comment_cat`
--

CREATE TABLE `comment_cat` (
  `comment_cat_id` int(11) NOT NULL,
  `comment_cat_name` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comment_cat`
--

INSERT INTO `comment_cat` (`comment_cat_id`, `comment_cat_name`) VALUES
(1, 'عمومی');

-- --------------------------------------------------------

--
-- Table structure for table `last_url_with_page`
--

CREATE TABLE `last_url_with_page` (
  `url_with_page_id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `last_url_with_page`
--

INSERT INTO `last_url_with_page` (`url_with_page_id`, `url_id`) VALUES
(1, 33);

-- --------------------------------------------------------

--
-- Table structure for table `options`
--

CREATE TABLE `options` (
  `option_id` int(11) NOT NULL,
  `owner_insta_user` varchar(191) NOT NULL,
  `owner_insta_pass` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `options`
--

INSERT INTO `options` (`option_id`, `owner_insta_user`, `owner_insta_pass`) VALUES
(1, 'solace.iran.shop', 'XX99100xx');

-- --------------------------------------------------------

--
-- Table structure for table `search_terms`
--

CREATE TABLE `search_terms` (
  `search_term_id` int(11) NOT NULL,
  `serch_title` varchar(191) NOT NULL,
  `search_desc` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `search_terms`
--

INSERT INTO `search_terms` (`search_term_id`, `serch_title`, `search_desc`) VALUES
(1, '#احمد_کلاته', 'رشد پیج');

-- --------------------------------------------------------

--
-- Table structure for table `urls`
--

CREATE TABLE `urls` (
  `id` int(11) NOT NULL,
  `url` varchar(191) NOT NULL,
  `description` text DEFAULT NULL,
  `belongs_to` varchar(191) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `urls`
--

INSERT INTO `urls` (`id`, `url`, `description`, `belongs_to`, `date`) VALUES
(1, 'https://www.instagram.com/p/CTsHtjMIvQ2/', 'posts', 'https://www.instagram.com/bari.editor/', '2021-10-11 10:00:06'),
(2, 'https://www.instagram.com/p/CUehJDtsTgm/', 'posts', 'https://www.instagram.com/ahmad_kalateha/', '2021-10-11 10:00:06'),
(3, 'https://www.instagram.com/p/CSeSk4Sg-Cy/', 'posts', 'https://www.instagram.com/razeparesh/', '2021-10-11 10:00:06'),
(4, 'https://www.instagram.com/p/CUUxYoSoKtB/', 'posts', 'https://www.instagram.com/it_homayoon/', '2021-10-11 10:00:06'),
(5, 'https://www.instagram.com/p/CR04ZeLi5cj/', 'posts', 'https://www.instagram.com/ghanone.jazb.kaenat/', '2021-10-11 10:00:06'),
(6, 'https://www.instagram.com/p/CUAxc51gkEK/', 'posts', 'https://www.instagram.com/adobino.ir/', '2021-10-11 10:00:06'),
(7, 'https://www.instagram.com/p/CQOi4tZFpAU/', 'posts', 'https://www.instagram.com/alipirgharebaghi/', '2021-10-11 10:00:06'),
(8, 'https://www.instagram.com/p/CTIiejJITxU/', 'posts', 'https://www.instagram.com/arameshe_khodai/', '2021-10-11 10:00:06'),
(9, 'https://www.instagram.com/p/CSJ9FVps3qz/', 'posts', 'https://www.instagram.com/saeedadelian_tabib/', '2021-10-11 10:00:06'),
(10, 'https://www.instagram.com/p/CU4Iy75oARP/', 'posts', 'https://www.instagram.com/mah_dimahmodi1382/', '2021-10-11 10:00:06'),
(11, 'https://www.instagram.com/p/CU4ITJctqCs/', 'posts', 'https://www.instagram.com/odkolonshopp/', '2021-10-11 10:00:06'),
(12, 'https://www.instagram.com/p/CU4G5Jog593/', 'posts', 'https://www.instagram.com/jazbe.binahayat/', '2021-10-11 10:00:06'),
(13, 'https://www.instagram.com/p/CU3IovOq3Qe/', 'posts', 'https://www.instagram.com/amirhossein_grafist.ir/', '2021-10-11 10:00:06'),
(14, 'https://www.instagram.com/p/CU3APsGq32H/', 'posts', 'https://www.instagram.com/raz_afarinesh7/', '2021-10-11 10:00:06'),
(15, 'https://www.instagram.com/p/CU253x3BmHU/', 'posts', 'https://www.instagram.com/auto_staar/', '2021-10-11 10:00:07'),
(16, 'https://www.instagram.com/p/CU20v2RBAL5/', 'posts', 'https://www.instagram.com/meta_motivational/', '2021-10-11 10:00:07'),
(17, 'https://www.instagram.com/p/CU21UvKoBFm/', 'posts', 'https://www.instagram.com/mrhedayati_official/', '2021-10-11 10:00:07'),
(18, 'https://www.instagram.com/p/CU2z91-Itvu/', 'posts', 'https://www.instagram.com/admin_a_maryam/', '2021-10-11 10:00:07'),
(19, 'https://www.instagram.com/p/CU2xAJ1I0ri/', 'posts', 'https://www.instagram.com/ham_timi/', '2021-10-11 10:00:07'),
(20, 'https://www.instagram.com/p/CU2w1clo0r4/', 'posts', 'https://www.instagram.com/social_arva/', '2021-10-11 10:00:07'),
(21, 'https://www.instagram.com/p/CU2tJeoMZem/', 'posts', 'https://www.instagram.com/admin.hosna/', '2021-10-11 10:00:07'),
(22, 'https://www.instagram.com/p/CU2qSTYI8w2/', 'posts', 'https://www.instagram.com/social.faeze/', '2021-10-11 10:00:07'),
(23, 'https://www.instagram.com/p/CU2iszEIAvp/', 'posts', 'https://www.instagram.com/yousef.zolfagharii/', '2021-10-11 10:00:07'),
(24, 'https://www.instagram.com/p/CU2f-19otBi/', 'posts', 'https://www.instagram.com/fekremossbatt/', '2021-10-11 10:00:07'),
(25, 'https://www.instagram.com/p/CU2YKtjgLuw/', 'posts', 'https://www.instagram.com/ahmad_kalaathe/', '2021-10-11 10:00:07'),
(26, 'https://www.instagram.com/p/CU2XvHUj17y/', 'posts', 'https://www.instagram.com/ghalam.rah/', '2021-10-11 10:00:07'),
(27, 'https://www.instagram.com/p/CU2WKOghyAz/', 'posts', 'https://www.instagram.com/mr.fat_yazd/', '2021-10-11 10:00:07'),
(28, 'https://www.instagram.com/p/CU2DvkEIw-N/', 'posts', 'https://www.instagram.com/jadeh_tandorosti/', '2021-10-11 10:00:07'),
(29, 'https://www.instagram.com/p/CU1mPOsNQxW/', 'posts', 'https://www.instagram.com/karyabikamkar/', '2021-10-11 10:00:07'),
(30, 'https://www.instagram.com/p/CU0WFoBjJFx/', 'posts', 'https://www.instagram.com/angizeshi_ftn1984/', '2021-10-11 10:00:07'),
(31, 'https://www.instagram.com/p/CU0VITzg8py/', 'posts', 'https://www.instagram.com/dore_kalaate/', '2021-10-11 10:00:07'),
(32, 'https://www.instagram.com/p/CU0UoPJqGWG/', 'posts', 'https://www.instagram.com/vanadium_abzar/', '2021-10-11 10:00:07'),
(33, 'https://www.instagram.com/p/CU0RQnPow6p/', 'posts', 'https://www.instagram.com/admin.fatiima/', '2021-10-11 10:00:07'),
(34, 'https://www.instagram.com/ahmad_kalateha/', 'pages', '', '2021-10-11 10:01:28'),
(35, 'https://www.instagram.com/razeparesh/', 'pages', '', '2021-10-11 10:01:41'),
(36, 'https://www.instagram.com/it_homayoon/', 'pages', '', '2021-10-11 10:01:53'),
(37, 'https://www.instagram.com/ghanone.jazb.kaenat/', 'pages', '', '2021-10-11 10:02:04'),
(38, 'https://www.instagram.com/adobino.ir/', 'pages', '', '2021-10-11 10:02:16'),
(39, 'https://www.instagram.com/alipirgharebaghi/', 'pages', '', '2021-10-11 10:02:28'),
(40, 'https://www.instagram.com/arameshe_khodai/', 'pages', '', '2021-10-11 10:02:39'),
(41, 'https://www.instagram.com/saeedadelian_tabib/', 'pages', '', '2021-10-11 10:02:52'),
(42, 'https://www.instagram.com/mah_dimahmodi1382/', 'pages', '', '2021-10-11 10:03:03'),
(43, 'https://www.instagram.com/odkolonshopp/', 'pages', '', '2021-10-11 10:03:14'),
(44, 'https://www.instagram.com/jazbe.binahayat/', 'pages', '', '2021-10-11 10:03:26'),
(45, 'https://www.instagram.com/amirhossein_grafist.ir/', 'pages', '', '2021-10-11 10:03:38'),
(46, 'https://www.instagram.com/raz_afarinesh7/', 'pages', '', '2021-10-11 10:03:49'),
(47, 'https://www.instagram.com/auto_staar/', 'pages', '', '2021-10-11 10:04:00'),
(48, 'https://www.instagram.com/meta_motivational/', 'pages', '', '2021-10-11 10:04:11'),
(49, 'https://www.instagram.com/mrhedayati_official/', 'pages', '', '2021-10-11 10:04:23'),
(50, 'https://www.instagram.com/admin_a_maryam/', 'pages', '', '2021-10-11 10:04:36'),
(51, 'https://www.instagram.com/ham_timi/', 'pages', '', '2021-10-11 10:04:47'),
(52, 'https://www.instagram.com/social_arva/', 'pages', '', '2021-10-11 10:04:59'),
(53, 'https://www.instagram.com/admin.hosna/', 'pages', '', '2021-10-11 10:05:10'),
(54, 'https://www.instagram.com/social.faeze/', 'pages', '', '2021-10-11 10:05:21'),
(55, 'https://www.instagram.com/yousef.zolfagharii/', 'pages', '', '2021-10-11 10:05:33'),
(56, 'https://www.instagram.com/fekremossbatt/', 'pages', '', '2021-10-11 10:05:44'),
(57, 'https://www.instagram.com/ahmad_kalaathe/', 'pages', '', '2021-10-11 10:05:56'),
(58, 'https://www.instagram.com/ghalam.rah/', 'pages', '', '2021-10-11 10:06:07'),
(59, 'https://www.instagram.com/mr.fat_yazd/', 'pages', '', '2021-10-11 10:06:19'),
(60, 'https://www.instagram.com/jadeh_tandorosti/', 'pages', '', '2021-10-11 10:06:30'),
(61, 'https://www.instagram.com/karyabikamkar/', 'pages', '', '2021-10-11 10:06:41'),
(62, 'https://www.instagram.com/angizeshi_ftn1984/', 'pages', '', '2021-10-11 10:06:52'),
(63, 'https://www.instagram.com/dore_kalaate/', 'pages', '', '2021-10-11 10:07:05'),
(64, 'https://www.instagram.com/vanadium_abzar/', 'pages', '', '2021-10-11 10:07:18'),
(65, 'https://www.instagram.com/admin.fatiima/', 'pages', '', '2021-10-11 10:07:47');

-- --------------------------------------------------------

--
-- Table structure for table `url_activity`
--

CREATE TABLE `url_activity` (
  `id` int(11) NOT NULL,
  `option_id` int(11) NOT NULL,
  `url_id` int(11) NOT NULL,
  `f_activity_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `url_cat`
--

CREATE TABLE `url_cat` (
  `id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `search_term` varchar(191) NOT NULL,
  `blong_to` varchar(191) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activites`
--
ALTER TABLE `activites`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comment_cat`
--
ALTER TABLE `comment_cat`
  ADD PRIMARY KEY (`comment_cat_id`);

--
-- Indexes for table `last_url_with_page`
--
ALTER TABLE `last_url_with_page`
  ADD PRIMARY KEY (`url_with_page_id`);

--
-- Indexes for table `options`
--
ALTER TABLE `options`
  ADD PRIMARY KEY (`option_id`);

--
-- Indexes for table `search_terms`
--
ALTER TABLE `search_terms`
  ADD PRIMARY KEY (`search_term_id`);

--
-- Indexes for table `urls`
--
ALTER TABLE `urls`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `url` (`url`);

--
-- Indexes for table `url_activity`
--
ALTER TABLE `url_activity`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `url_cat`
--
ALTER TABLE `url_cat`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activites`
--
ALTER TABLE `activites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `comment_cat`
--
ALTER TABLE `comment_cat`
  MODIFY `comment_cat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `last_url_with_page`
--
ALTER TABLE `last_url_with_page`
  MODIFY `url_with_page_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `options`
--
ALTER TABLE `options`
  MODIFY `option_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `search_terms`
--
ALTER TABLE `search_terms`
  MODIFY `search_term_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `urls`
--
ALTER TABLE `urls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `url_activity`
--
ALTER TABLE `url_activity`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `url_cat`
--
ALTER TABLE `url_cat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
