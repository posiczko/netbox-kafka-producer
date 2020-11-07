from extras.plugins import PluginConfig


class NetboxKafkaProducerConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Animal Sounds plugin.
    """
    # Plugin package name
    name = 'netbox_kafka_producer'

    # Human-friendly name and description
    verbose_name = 'Netbox Kafka producer'
    description = 'Easily publish NetBox changes to Kafka'

    # Plugin version
    version = '1.0.27'

    # Plugin author
    author = 'Eric Busto',
    author_email = 'ebusto@nvidia.com',

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = []

    # Default configuration parameter values, if not set by the user
    default_settings = {
    }

    # Base URL path. If not set, the plugin name will be used.

    # Caching config
    caching_config = {}

    middleware = ("netbox_kafka_producer.middleware.KafkaChangeMiddleware",)

    default_settings = {
        'kafka': {
            'servers': 'kafka1:9092,kafka2:9092',
            'topic': 'netbox',
        },
    }


config = NetboxKafkaProducerConfig
