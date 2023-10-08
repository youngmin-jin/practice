# Apache Kafka
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
   > bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092 <br/><br/>
   > *--partitions 2 can be specified if want to create two partitions <br/>
   > *bin/kafka-topics.sh --bootstrap-server localhost:9092 --list can show the list of all topics <br/>
   > *bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic topicname shows the details of the topic

6. start a producer to send messages to kafka
   > bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092 <br/><br/>
   > *if the producer starts, you get '>' prompt. type any msg and press enter <br/>
   > ![image](https://github.com/youngmin-jin/practice/assets/135728064/21f71c71-220e-4a25-bc3f-c5538767b9c9) 

   - start a producer with message keys (can be used to extract the value of JSON data)
      > bin/kafka-console-producer.sh --topic topicname --bootstrap-server localhost:9092 --property parse.key=true --property key.separator=: <br/><br/>
      > *partitions are published in order (e.g., partition 0-> partition 1-> partition 0..) <br/>
      > *msgs with the same key will always be published to the same partition, and preserved in order <br/>
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/7ff9a92a-9366-4dfa-8bb9-fc89b414f86a)


7. start a consumer to read messages from kafka (new terminal)
   > cd kafka_2.12-2.8.0 <br/>
   > bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092 <br/><br/>
   > *can see the msg sent from the producer in real time <br/>
   > ![image](https://github.com/youngmin-jin/practice/assets/135728064/388dd58c-d619-4990-a9e8-c21e0eb9e800) <br/><br/>
   > *if --from-beginning does not exist, the consumer only receives the msg after the connection 

   - start a consumer with group
      > *can see the details of the group <br/>
      > bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group atm-app <br/><br/>
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/53d8ea70-dce2-47b8-9b2c-47addae804e5) <br/>
      > *CURRENT-OFFSET: shows the final queue of consumed msgs <br/>
      > *LOG-END-OFFSET: shows the last queue of the whole msgs including unconsumed msgs <br/>
      > *LAG: shows unconsumed msgs <br/><br/>
      
      > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app <br/><br/>
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/0528c2a0-dd4e-4868-851e-3d090fb9cbe6) <br/>
      > *shows the unconsumed msgs

   - reset offsets (when wanting to consume the msgs again from the beginning)
      > bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --to-earliest --execute <br/><br/>
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/349e7120-f7d7-4bb1-88d8-26faa4fb2053) <br/>
      > *--reset-offsets --shift-by -2 lefts 2 unconsumed msgs


<br/><br/>
- directory
  - bin: shell scripts to control kafka and zookeeper
  - config: configuration files
  - logs: log files for kafka and zookeeper/ _msgs are stored here_ <br/>

- how to use kafka in python
  - refer to coursera_ETL_and_data_pipelines_with_shell_airflow_kafka/Kafka Python Client.pdf  
