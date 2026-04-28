module DiagnosticsSample exposing (brokenFactory, brokenConsumer)

brokenFactory : String
brokenFactory =
    missingGreeting

brokenConsumer : String
brokenConsumer =
    missingConsumerValue
