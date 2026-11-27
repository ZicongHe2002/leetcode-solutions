class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        positions = {skill: index for index, skill in enumerate(req_skills)}
        best = {0: ()}
        for person, skills in enumerate(people):
            coverage = 0
            for skill in skills:
                if skill in positions:
                    coverage |= 1 << positions[skill]
            if coverage == 0:
                continue
            for mask, team in list(best.items()):
                combined = mask | coverage
                candidate = team + (person,)
                if combined not in best or len(candidate) < len(best[combined]):
                    best[combined] = candidate
        return list(best[(1 << len(req_skills)) - 1])
