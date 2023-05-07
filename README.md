# Greengrass Software Catalog

The Greengrass Software Catalog is an index of Greengrass components that are developed by the Greengrass community. Build your edge applications faster by using this catalog to find pre-built components that best fit your use-case.

- [Catalog](#catalog)
    - [Community components](#community-components)
    - [AWS provided components](#aws-provided-components)
- [Resources](#resources)
    - [Tools](#tools)
    - [Documentation](#documentation)
- [License](#license)

## Catalog

### Community components

The Greengrass developer community builds and maintains components that you can deploy to your devices. Instead of building components for each required capability, you can choose components from the catalog to kick-start your IoT project. Since these components are a reference implementation of common patterns, please ensure that you appropriately review and test any functionality before deploying it to your production environments.

To request a feature or report a bug, open a GitHub issue on the repository for that component. Note: AWS does not guarantee support for the community components. Please check the corresponding CONTRIBUTING file for details.

Following is a list of Greengrass components.
* [Kinesis Video Streams](https://github.com/awslabs/aws-greengrass-labs-kvs-stream-uploader): This component ingests audio and video streams from RTSP cameras connected to the Greengrass core device. The audio and video streams are then uploaded to Amazon Kinesis Video Streams.
* [Modbus TCP](https://github.com/awslabs/aws-greengrass-labs-modbus-tcp-protocol-adapter): This component collects data from local devices through the ModbusTCP protocol and publishes it to selected data streams.
* [Bluetooth IoT Gateway](https://github.com/awslabs/aws-greengrass-labs-bluetooth-gateway): The BLE IoT Gateway component uses the [BluePy](https://ianharvey.github.io/bluepy-doc/index.html) library (Python module which allows communication with Bluetooth Low Energy devices) to create the BLE client interface.
* [Home Assistant](https://github.com/awslabs/aws-greengrass-labs-component-for-home-assistant): This component enables use cases where the customer desires [Home Assistant](https://www.home-assistant.io/) for local control of their smart home devices. This component enables deep integration with AWS services at the edge and in the cloud, to deliver powerful home automation solutions that extend Home Assistant’s capabilities.
* [InfluxDBGrafana Dashboard](https://github.com/awslabs/aws-greengrass-labs-dashboard-influxdb-grafana): This component provides a one-click experience for the below [InfluxDB](https://github.com/awslabs/aws-greengrass-labs-database-influxdb) and [Grafana](https://github.com/awslabs/aws-greengrass-labs-dashboard-grafana) components, connecting InfluxDB to Grafana and automating the setup of a local Grafana dashboard rendering Greengrass telemetry in real-time.
* [InfluxDB](https://github.com/awslabs/aws-greengrass-labs-database-influxdb): This component provides support for [InfluxDB](https://www.influxdata.com/products/influxdb/) time-series database at the edge. Customers can use this component to support processing data from IoT sensors, carry out real-time analytics and monitor edge operations.
* [InfluxDB Publisher](https://github.com/awslabs/aws-greengrass-labs-telemetry-influxdbpublisher): This component relays Greengrass System Health Telemetry from the [Nucleus emitter plugin](https://github.com/aws-greengrass/aws-greengrass-telemetry-nucleus-emitter) to InfluxDB. You can also use this component to forward custom telemetry to InfluxDB.
* [Grafana](https://github.com/awslabs/aws-greengrass-labs-dashboard-grafana): This component provides support for the Grafana visualization dashboard at the edge. Customers can use this component to visualize data locally. This component can be used to render data from the InfluxDB component.
* [IoT PubSub SDK for Python](https://github.com/awslabs/aws-greengrass-labs-iot-pubsub-sdk-for-python): This project provides an IoT PubSub application architecture delivered as a Python library to simplify and accelerate development of [distributed IoT applications built on AWS IoT Greengrass Components](https://aws.amazon.com/blogs/iot/using-the-aws-greengrass-pubsub-sdk-to-develop-distributed-iot-pubsub-applications/)
* [Jupyter Labs](https://github.com/awslabs/aws-greengrass-labs-jupyterlab): This component deploys JupyterLab to a Greengrass core device. The Jupyter environment will have access to all the process and environment variable resources set by Greengrass thereby simplifying the process of testing and developing components written in Python.
* [Local Webserver](https://github.com/awslabs/aws-greengrass-labs-local-web-server): This component enable users to create local web user interface on a Greengrass core device. The web user interface can be used to configure device and application settings, or monitoring the device.
* [LoRaWAN Network Server](https://github.com/awslabs/aws-greengrass-labs-component-for-the-things-stack-lorawan): This component deploys [The Things Stack](https://github.com/TheThingsNetwork/lorawan-stack) LoRaWAN Network Server (LNS). This enables ingestion of data from LoRaWAN devices so customers can get insights from data and take action locally without connecting to the cloud.
* [TES Routing to Container](https://github.com/awslabs/aws-greengrass-labs-tes-router): This component configures nftables or iptables on a Greengrass device to be able to use [Token Exchange Service](https://docs.aws.amazon.com/greengrass/v2/developerguide/token-exchange-service-component.html) component with containers.
* [WebRTC](https://github.com/awslabs/aws-greengrass-labs-webrtc): This component ingests audio and video streams from RTSP cameras connected to the Greengrass core device. And then the component turns the audio and video streams into peer-to-peer communication or relay through Amazon Kinesis Video Streams.
* [GStreamer for LookoutForVision](https://github.com/awslabs/aws-greengrass-labs-lookoutvision-gstreamer): This component provides a GStreamer plugin that enables you to perform [Amazon Lookout For Vision](https://aws.amazon.com/lookout-for-vision/) anomaly detection in your custom GStreamer pipelines.
* [Postgresql DB](https://github.com/awslabs/aws-greengrass-labs-database-postgresql): This component provides support for [postgresql](https://www.postgresql.org/) relation database at the edge. Customers can use this component to provision and manage a local PostgreSQL instance inside a docker container. 
* [Secrets Manager client](https://github.com/awslabs/aws-greengrass-labs-secretsmanagerclient): This component provides a CLI tool that can be used by other components needing to retrieve secrets from the SecretManager component in a recipe lifecycle script.
* [Containerized Secure Tunneling](https://github.com/awslabs/aws-greengrass-labs-containerized-secure-tunneling): This component provides a Docker container for Secure Tunneling with all dependencies and matching libraries in a reusable and customizable recipe without relying on a specific host operating system.
* [S3 file uploader](https://github.com/awslabs/aws-greengrass-labs-s3-file-uploader): This component monitors a directory for new files, upload them to S3 and delete them upon successful upload.
* [Node-RED](https://github.com/awslabs/aws-greengrass-labs-nodered): This component installs Node-RED on the Greengrass core device using NPM. This component depends on the [Node-RED Auth](https://github.com/awslabs/aws-greengrass-labs-nodered-auth) component which must be explicitly deployed and configured. To deploy Node-RED flows to AWS Greengrass devices running Node-RED you can take advantage of [Node-RED CLI for Greengrass](https://github.com/awslabs/aws-greengrass-labs-node-red-app-cli)
* [Node-RED Docker](https://github.com/awslabs/aws-greengrass-labs-nodered-docker): This component installs Node-RED on the Greengrass core device using the official Node-RED docker container. This component depends on the [Node-RED Auth](https://github.com/awslabs/aws-greengrass-labs-nodered-auth) component which must be explicitly deployed and configured. To deploy Node-RED flows to AWS Greengrass devices running Node-RED you can take advantage of [Node-RED CLI for Greengrass](https://github.com/awslabs/aws-greengrass-labs-node-red-app-cli)
* [Node-RED Auth](https://github.com/awslabs/aws-greengrass-labs-nodered-auth): This component configure a user name and password to secure the Node-RED instance running 


### AWS provided components

AWS IoT Greengrass provides and maintains components that you can deploy to your devices. Below is the list of open source AWS-provided components. You can find the full list of components in the [AWS IoT Greengrass Developer Guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/public-components.html). Use the Greengrass console or API to deploy these components to your Greengrass core devices.

* [Greengrass nucleus](https://github.com/aws-greengrass/aws-greengrass-nucleus): The Greengrass nucleus component is a mandatory component and the minimum requirement to run the AWS IoT Greengrass Core software on a device.
* [Client device auth](https://github.com/aws-greengrass/aws-greengrass-client-device-auth): The client device auth component authenticates client devices and authorizes client device actions.
* [CloudWatch metrics](https://github.com/aws-greengrass/aws-greengrass-cloudwatch-metrics): The Amazon CloudWatch metrics component publishes custom metrics from Greengrass core devices to Amazon CloudWatch.
* [Device Defender](https://github.com/aws-greengrass/aws-greengrass-device-defender): The Device Defender component notifies administrators about changes in the state of Greengrass core devices.
* [Docker application manager](https://github.com/aws-greengrass/aws-greengrass-nucleus/tree/main/src/main/java/com/aws/greengrass/componentmanager/plugins/docker): The Docker application manager component enables AWS IoT Greengrass to download Docker images from public image registries. This component is built into the Greengrass nucleus.
* [IP detector](https://github.com/aws-greengrass/aws-greengrass-ip-detector): The IP detector component monitors the Greengrass core device's network connectivity information and updates the core device's connectivity information in the AWS IoT Greengrass cloud service.
* [Local debug console](https://github.com/aws-greengrass/aws-greengrass-localdebugconsole): The local debug console component provides a local dashboard that displays information about your AWS IoT Greengrass core devices and its components. You can use this dashboard to debug your core device and manage local components.
* [Log manager](https://github.com/aws-greengrass/aws-greengrass-log-manager): The log manager component uploads logs from AWS IoT Greengrass core devices to Amazon CloudWatch Logs. You can upload logs from the Greengrass nucleus, other Greengrass components, and other applications and services that aren't Greengrass components.
* [MQTT bridge](https://github.com/aws-greengrass/aws-greengrass-mqtt-bridge): The MQTT bridge component relays MQTT messages between client devices, local Greengrass publish/subscribe, and AWS IoT Core. You can use this component to act on MQTT messages from client devices in custom components and sync client devices with the AWS Cloud.
* [MQTT broker (Moquette)](https://github.com/aws-greengrass/aws-greengrass-moquette-mqtt): The Moquette MQTT broker component handles MQTT messages between client devices and a Greengrass core device. This component provides a modified version of the Moquette MQTT broker (https://github.com/moquette-io/moquette).
* [Nucleus telemetry emitter](https://github.com/aws-greengrass/aws-greengrass-telemetry-nucleus-emitter): The nucleus emitter component gathers system health telemetry data and publishes it continually to a local topic and an AWS IoT Core MQTT topic. This component enables you to gather real-time system telemetry on your Greengrass core devices.
* [Secret manager](https://github.com/aws-greengrass/aws-greengrass-secret-manager) The secret manager component deploys secrets from AWS Secrets Manager to Greengrass core devices. Use this component to securely use credentials, such as passwords, in custom components on your Greengrass core devices.
* [Shadow manager](https://github.com/aws-greengrass/aws-greengrass-shadow-manager) The shadow manager component enables the local shadow service on your core device. The local shadow service allows components to use interprocess communication to [interact with local shadows.](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-local-shadows.html)  The shadow manager component manages the storage of local shadow documents, and also handles synchronization of local shadow states with the AWS IoT Device Shadow service.


## Resources

### Tools

The AWS IoT Greengrass team maintains the following tools that you can use to develop, test, and deploy Greengrass components.

* [Greengrass Development Kit CLI](https://github.com/aws-greengrass/aws-greengrass-gdk-cli): Use this [CLI](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-development-kit-cli.html) in your local development environment to kickstart new component development using various component templates. You can use the GDK CLI to build the component locally and publish the component to your AWS account as a private component.
* [Greengrass CLI](https://github.com/aws-greengrass/aws-greengrass-cli): Use this [CLI](https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-cli.html) on your core device to debug and deploy public/private components. The Greengrass CLI is a component that you can deploy to your core devices to create local deployments, view details about installed components, and explore log files.

### Documentation

See the [Greengrass V2 developer guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) and the [Greengrass V2 API reference](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html) to learn more about the features that you can leverage to create components and applications for your use case.

## License

This catalog is licensed under the CC BY-SA 4.0 License. 
