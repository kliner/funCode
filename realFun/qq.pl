#!/usr/bin/env perl
use lib '/Users/kliner/github/Mojo-Webqq/lib';
use Mojo::Webqq;

my ($host,$port,$post_api);

$host = "0.0.0.0"; #发送消息接口监听地址，没有特殊需要请不要修改
$port = 5000;      #发送消息接口监听端口，修改为自己希望监听的端口
$post_api = 'http://localhost:8888/api';  #接收到的消息上报接口，如果不需要接收消息上报，可以删除或注释此行

my $client = Mojo::Webqq->new(ignore_retcode=>[1202,100100]);
$client->load("ShowMsg");
$client->load("Openqq",data=>{
        listen=>[{host=>$host,port=>$port}], 
        post_api=>$post_api,
        post_event=>1,
        post_event_list=>['login','stop','state_change','input_qrcode','new_group','new_friend','new_group_member','lose_group','lose_friend','lose_group_member']
    });
$client->run();
