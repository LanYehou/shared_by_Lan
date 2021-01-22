pip install shadowsocks
cd /etc
echo "{" > ss.json
echo '"server":"0.0.0.0", ' >> ss.json
echo '"server_port":8388,' >> ss.json
echo '"local_address":"127.0.0.1",' >> ss.json
echo '"password":"l123456/",' >> ss.json
echo '"timeout":300,' >> ss.json
echo '"method":"aes-256-cfb",' >> ss.json
echo '"fast_open":false,' >> ss.json
echo '"workers":1' >> ss.json
echo "}" >> ss.json
ssserver -c /etc/ss.json -d start
