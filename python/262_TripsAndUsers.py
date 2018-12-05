# select Request_at as Day,
#       ROUND(sum(Status = 'cancelled_by_driver' or Status = 'cancelled_by_client') / count(t.id), 2)  as 'Cancellation Rate'
# from Trips t join Users u on t.Client_Id = u.Users_Id and u.Banned = 'No'
# where Request_at >= '2013-10-01' and Request_at <= '2013-10-03'
# group by Request_at;
