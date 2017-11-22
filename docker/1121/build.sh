#!/bin/sh
rm *.jar
cd ../..
mvn -Dmaven.test.skip=true -U clean package
cd -
pwd
cp ../../target/tank-1.0-SNAPSHOT-jar-with-dependencies.jar .
docker build -t docker-hack.ele.me/zhiming.rong/beta-tank:2.0 .