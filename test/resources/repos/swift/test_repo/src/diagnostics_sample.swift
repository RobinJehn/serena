func brokenFactory() -> String {
    missingGreeting
}

func brokenConsumer() {
    print(brokenFactory())
    print(missingConsumerValue)
}
