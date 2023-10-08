# Send messages using Kafka
1. download kafka and extract kafka from the zip file creating a new directory 'kafka_2.12-2.8.0'
   > wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

2. extract kafka from the zip file
   > tar -xzf kafka_2.12-2.8.0.tgz

3. start the ZooKeeper server (new terminal)
   > cd kafka_2.12-2.8.0 <br/>
   > bin/zookeeper-server-start.sh config/zookeeper.properties

4. start the kafka broker service (new terminal)
   > cd kafka_2.12-2.8.0 <br/>
   > bin/kafka-server-start.sh config/server.properties

5. create a topic called "news" (new terminal)
   > cd kafka_2.12-2.8.0 <br/>
   > bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

6. start a producer to send messages to kafka
   > bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092 <br/><br/>
   > *if the producer starts, you get '>' prompt. type any msg and press enter <br/>
   > ![image](https://github.com/youngmin-jin/practice/assets/135728064/21f71c71-220e-4a25-bc3f-c5538767b9c9)

7. start a consumer to read messages from kafka (new terminal)
   > cd kafka_2.12-2.8.0 <br/>
   > bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092 <br/><br/>
   > *can see the msg sent from the producer in real time <br/>
   > ![image](https://github.com/youngmin-jin/practice/assets/135728064/388dd58c-d619-4990-a9e8-c21e0eb9e800) <br/><br/>
   > *if --from-beginning does not exist, the consumer only receives the msg after the connection 

- directory
  - bin: shell scripts to control kafka and zookeeper
  - config: configuration files
  - logs: log files for kafka and zookeeper/ _msgs are stored here_

   