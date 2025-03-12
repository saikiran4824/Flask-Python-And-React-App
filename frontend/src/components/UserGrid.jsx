import { Flex, Grid, Spinner, Text } from "@chakra-ui/react";

import UserCard from "./UserCard";
import { useEffect, useState } from "react";
import { BASE_URL } from "../App";

const UserGrid = ({ users, setUsers }) => {
	const [isLoading, setIsLoading] = useState(true);

	useEffect(() => {
		const getUsers = async () => {
			try {
				const res = await fetch(BASE_URL + "/friends");
				const data = await res.json();

				if (!res.ok) {
					throw new Error(data.error);
				}
				setUsers(data);
			} catch (error) {
				console.error(error);
			} finally {
				setIsLoading(false);
			}
		};
		getUsers();
	}, [setUsers]);

	console.log(users);
	return (
		<>
			<Grid
				templateColumns={{
					base: "1fr",
					md: "repeat(2, 1fr)",
					lg: "repeat(3, 1fr)",
				}}
				gap={4}
			>
				{users.map((user) => (
					<UserCard key={user.id} user={user} setUsers={setUsers} />
				))}
			</Grid>

			{isLoading && (
				<Flex justifyContent={"center"}>
					<Spinner size={"xl"} />
				</Flex>
			)}
			{!isLoading && users.length === 0 && (
				<Flex justifyContent={"center"}>
					<Text fontSize="30px"
      fontWeight="bold"
      color="pink.400"
      textShadow="2px 2px 6px rgba(0, 0, 0, 0.2)"
      letterSpacing="wide">

						No Notes Found.
					</Text>
				</Flex>
			)}
		</>
	);
};
export default UserGrid;
