#include "../include/amjuel_hyd_ionisation.hxx"

/// Coefficients to calculate the reaction rate <σv>
/// Reaction 2.1.5, Amjuel page 135
/// E-index varies fastest, so coefficient is [T][n]
static constexpr const BoutReal rate_coefs[9][9] = {
    {-32.4802533034, -0.05440669186583, 0.09048888225109, -0.04054078993576,
     0.008976513750477, -0.001060334011186, 6.846238436472e-05, -2.242955329604e-06,
     2.890437688072e-08},
    {14.2533239151, -0.0359434716076, -0.02014729121556, 0.0103977361573,
     -0.001771792153042, 0.0001237467264294, -3.130184159149e-06, -3.051994601527e-08,
     1.888148175469e-09},
    {-6.632235026785, 0.09255558353174, -0.005580210154625, -0.005902218748238,
     0.001295609806553, -0.0001056721622588, 4.646310029498e-06, -1.479612391848e-07,
     2.85225125832e-09},
    {2.059544135448, -0.07562462086943, 0.01519595967433, 0.0005803498098354,
     -0.0003527285012725, 3.201533740322e-05, -1.835196889733e-06, 9.474014343303e-08,
     -2.342505583774e-09},
    {-0.442537033141, 0.02882634019199, -0.00728577148505, 0.0004643389885987,
     1.145700685235e-06, 8.493662724988e-07, -1.001032516512e-08, -1.476839184318e-08,
     6.047700368169e-10},
    {0.06309381861496, -0.00578868653578, 0.00150738295525, -0.0001201550548662,
     6.574487543511e-06, -9.678782818849e-07, 5.176265845225e-08, 1.29155167686e-09,
     -9.685157340473e-11},
    {-0.005620091829261, 0.000632910556804, -0.0001527777697951, 8.270124691336e-06,
     3.224101773605e-08, 4.377402649057e-08, -2.622921686955e-09, -2.259663431436e-10,
     1.161438990709e-11},
    {0.0002812016578355, -3.564132950345e-05, 7.222726811078e-06, 1.433018694347e-07,
     -1.097431215601e-07, 7.789031791949e-09, -4.197728680251e-10, 3.032260338723e-11,
     -8.911076930014e-13},
    {-6.011143453374e-06, 8.089651265488e-07, -1.186212683668e-07, -2.381080756307e-08,
     6.271173694534e-09, -5.48301024493e-10, 3.064611702159e-11, -1.355903284487e-12,
     2.935080031599e-14}};

/// Coefficients to calculate the radiation energy loss
/// Reaction 2.1.5, Amjuel page 280
/// E-index varies fastest, so coefficient is [T][n]
static constexpr const BoutReal radiation_coefs[9][9] = {
    {-24.97580168306, 0.001081653961822, -0.0007358936044605, 0.0004122398646951,
     -0.0001408153300988, 2.46973083622e-05, -2.212823709798e-06, 9.648139704737e-08,
     -1.611904413846e-09},
    {10.04448839974, -0.003189474633369, 0.002510128351932, -0.0007707040988954,
     0.0001031309578578, -3.716939423005e-06, -4.249704742353e-07, 4.164960852522e-08,
     -9.893423877739e-10},
    {-4.867952931298, -0.00585226785069, 0.002867458651322, -0.0008328668093987,
     0.0002056134355492, -3.301570807523e-05, 2.831739755462e-06, -1.164969298033e-07,
     1.78544027879e-09},
    {1.689422238067, 0.007744372210287, -0.003087364236497, 0.000470767628842,
     -5.508611815406e-05, 7.305867762241e-06, -6.000115718138e-07, 2.045211951761e-08,
     -1.79031287169e-10},
    {-0.41035323201, -0.003622291213236, 0.001327415215304, -0.0001424078519508,
     3.307339563081e-06, 5.256679519499e-09, 7.597020291557e-10, 1.799505288362e-09,
     -9.280890205774e-11},
    {0.06469718387357, 0.0008268567898126, -0.0002830939623802, 2.41184802496e-05,
     5.7079848611e-07, -1.0169456933e-07, 3.517154874443e-09, -4.453195673947e-10,
     2.002478264932e-11},
    {-0.006215861314764, -9.836595524255e-05, 3.017296919092e-05, -1.474253805845e-06,
     -2.397868837417e-07, 1.518743025531e-08, 4.149084521319e-10, -6.803200444549e-12,
     -1.151855939531e-12},
    {0.000328980989546, 5.845697922558e-06, -1.479323780613e-06, -4.633029022577e-08,
     3.337390374041e-08, -1.770252084837e-09, -5.289806153651e-11, 3.86439477625e-12,
     -8.694978774411e-15},
    {-7.335808238917e-06, -1.367574486885e-07, 2.423236476442e-08, 5.733871119707e-09,
     -1.512777532459e-09, 8.733801272834e-11, 7.196798841269e-13, -1.441033650378e-13,
     1.734769090475e-15}};

void AmjuelHydIonisation::calculate_rates(Options& electron, Options& atom, Options& ion) {
  electron_reaction(electron, atom, ion, rate_coefs, radiation_coefs,
                    0.0 // Note: Ionisation potential included in radiation_coefs
  );
}
