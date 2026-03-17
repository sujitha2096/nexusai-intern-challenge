CREATE TABLE customer_interactions (
    id SERIAL PRIMARY KEY,
    customer_phone VARCHAR(20) NOT NULL,
    interaction_type VARCHAR(50) CHECK (interaction_type IN ('call', 'chat', 'email')),
    sentiment_score DECIMAL(3, 2), -- Range -1.00 to 1.00
    intent_detected VARCHAR(100),
    was_escalated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for performance
CREATE INDEX idx_customer_phone ON customer_interactions(customer_phone);
CREATE INDEX idx_created_at ON customer_interactions(created_at);