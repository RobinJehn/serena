function broken_factory()
    missingGreeting
end

function broken_consumer()
    value = broken_factory()
    missingConsumerValue
end
