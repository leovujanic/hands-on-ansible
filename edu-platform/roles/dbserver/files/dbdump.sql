SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `users` (`id`, `name`, `last_name`, `created_at`) VALUES
  (1, 'Pero', 'Peric', '2018-04-06 03:07:02'),
  (2, 'Marko', 'Marulic', '2018-04-06 03:07:02'),
  (3, 'Tomo', 'Tomic', '2018-04-06 03:07:02'),
  (4, 'Ivo', 'Ivić', '2018-04-06 03:07:02'),
  (5, 'Marko', 'Markić', '2018-04-06 03:07:02'),
  (6, 'Jura', 'Juric', '2018-04-06 03:07:02'),
  (7, 'Baka', 'Barica', '2018-04-06 03:07:02');


ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;COMMIT;
