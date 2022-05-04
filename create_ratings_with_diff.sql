DROP TABLE IF EXISTS ratings_with_diff; 
CREATE TABLE ratings_with_diff (userid numeric, movieid numeric, rating double precision, "time" numeric, avg_rating double precision, difference double precision);
insert into ratings_with_diff select r.userid, r.movieid, r.rating, r.time, a.avg, r.rating - a.avg as difference from ratings r, (select movieid, avg(rating) from ratings group by movieid) a where a.movieid = r.movieid group by r.userid, r.movieid, r.rating, r.time, a.avg, r.rating - a.avg;
