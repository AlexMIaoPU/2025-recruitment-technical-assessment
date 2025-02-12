//
//  MemoryLeakTracker.swift
//  FreeroomsAssessmentTests
//
//  Created by Anh Nguyen on 31/1/2025.
//

import Testing

struct MemoryLeakTracker<T: AnyObject> {
    weak var instance: T?
    var sourceLocation: SourceLocation
    
    func verifyDeallocation() {
        #expect(instance == nil, "Expected \(instance!) to be deallocated", sourceLocation: sourceLocation)
    }
}
