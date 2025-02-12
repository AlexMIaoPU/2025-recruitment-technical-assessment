//
//  RemoteBuilding.swift
//  FreeroomsAssessment
//
//  Created by Anh Nguyen on 31/1/2025.
//

import Foundation

public struct RemoteBuilding: Equatable, Codable {
    public let building_name: String
    public let building_id: UUID
    public let building_latitude: Double
    public let building_longitude: Double
    public let building_aliases: [String]
    
    public init(building_name: String, building_id: UUID, building_latitude: Double, building_longitude: Double, building_aliases: [String]) {
        self.building_name = building_name
        self.building_id = building_id
        self.building_latitude = building_latitude
        self.building_longitude = building_longitude
        self.building_aliases = building_aliases
    }
}
