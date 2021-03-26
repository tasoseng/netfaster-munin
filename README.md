```crontab -e -u munin
*/5 * * * *     /usr/local/sbin/netfaster3-stats.py
```

```
for i in $(/usr/local/share/munin/plugins/munin_netfaster3_ suggest);do
 echo ln -s /usr/local/share/munin/plugins/munin_netfaster3_ /usr/local/etc/munin/plugins/munin_netfaster3_${i}
done
```
